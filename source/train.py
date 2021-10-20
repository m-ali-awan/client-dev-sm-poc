# Imports

from fastai.basics import *
from fastai.callback.all import *
from fastai.vision.all import *
from fastai.medical.imaging import *

import pydicom

import pandas as pd

import argparse
import glob
import io
import logging
import os
import time

import requests
#import sagemaker_containers


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))





def train(args):
    
    logger.info("Implementing Train Function")
    path = Path(args.data_dir)
    b_size=args.batch_size
    
    items=get_dicom_files(path/f"train/")
    trn,val = RandomSplitter()(items)
    dicom_dataframe = pd.DataFrame.from_dicoms(items)
    df = pd.read_csv(path/f"labels.csv")


    df = pd.read_csv(path/f"labels.csv")

    logger.info("Making Dataloaders")
    pneumothorax = DataBlock(blocks=(ImageBlock(cls=PILDicom), CategoryBlock),
                   get_x=lambda x:path/f"{x[0]}",
                   get_y=lambda x:x[1],
                   batch_tfms=[*aug_transforms(size=224),Normalize.from_stats(*imagenet_stats)])

    dls = pneumothorax.dataloaders(df.values, num_workers=0,bs=b_size)
    
    logger.info("Defining Learner")
    learn = cnn_learner(dls, resnet34, metrics=accuracy)

    logger.info("Starting Training")
    learn.fit_one_cycle(1)

    
    logger.info("Saving the model.")
    model_path = Path(args.model_dir)
    print(f"Export model object")
    #learn.export(model_path / "export.pth")
    learn.save(model_path / "trained_learner_weights.pth")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()



    parser.add_argument(
        "--batch_size", type=int, default=4, metavar="BS", help="batch size (default: 4)"
    )
    parser.add_argument(
        "--lr",
        type=float,
        default=0.001,
        metavar="LR",
        help="initial learning rate (default: 0.001)")


    # Container environment
    parser.add_argument("--hosts", type=list, default=json.loads(os.environ["SM_HOSTS"]))
    parser.add_argument("--current-host", type=str, default=os.environ["SM_CURRENT_HOST"])
    parser.add_argument("--model-dir", type=str, default=os.environ["SM_MODEL_DIR"])
    parser.add_argument("--data-dir", type=str, default=os.environ["SM_CHANNEL_TRAINING"])
    parser.add_argument("--num-gpus", type=int, default=os.environ["SM_NUM_GPUS"])
    
    


    train(parser.parse_args())