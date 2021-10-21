


**Amazon SageMaker enables developers and data scientists to quickly and easily build, train, and deploy machine learning models at any scale.
Amazon SageMaker removes all the barriers that typically slow down developers who want to use machine learning.**



## Benefits of Sagemaker Studio:

> Starting a Studio notebook is faster than launching an instance-based notebook. Typically, it is 5-10 times faster than instance-based notebooks.

> Notebook sharing is an integrated feature in SageMaker Studio. Users can generate a shareable link that reproduces the notebook code and also the SageMaker image required to execute it, in just a few clicks.

> SageMaker Studio notebooks come pre-installed with the latest Amazon SageMaker Python SDK.

> SageMaker Studio notebooks are accessed from within Studio. This enables you to build, train, debug, track, and monitor your models without leaving Studio.

> Each member of a Studio team gets their own home directory to store their notebooks and other files. The directory is automatically mounted onto all instances and kernels as they're started, so their notebooks and other files are always available. The home directories are stored in Amazon Elastic File System (Amazon EFS) so that you can access them from other services.

> Studio notebooks are equipped with a set of predefined SageMaker image settings to get you started faster.

## Drawbacks of Sagemaker Studio:

> **As we know that script mode training, is one of the best features of Sagemaker, and converting a notebook code to work with script mode, usually envolves a no of
> debugging cycles, to make different environment variables work, etc(At least, if you haven't a lot of experience doing so). So, the LOCAL_MODE, comes to rescue in it.
> As we can quickly replicate the process, on local notebook instance, so we donot have to wait for 7-10 mins, as it happens once we are using external instances.
Now, LOCAL_MODE, cannot be used in Studio, as Studi Notebooks are themselves running in Docker, so we cannot have another docker container to replicate another process**

## Benefits of Studio over Notebook Instances:

> As swe know we can access our Notebook instances from Sagemake Console, same way we can access the Studio Notebooks, **WE ALSO HAVE THE OPTION OF SSO, SO WE CAN SIMPLY SAVE A 
> KIND OF BOOKMARK ADN THEN WITH SSO, WE CAN QUICKLY GET STRAIGHT TO THE STUDIO**

> With Notebook Instances, you can only access the notebooks if the notebook is started, **but with Studio Notebooks if you are not using any compute, and just want to review your code,
> you need not to start any instance, and wait for it, and also pay for it, you can simply review it, and you will only be billed when you will attach any compute resource with it.**

> Studio has EFS storage attached to it, so you can share the same storage with different kinds of instances, which yuo cannot do in simple Notebook Instances.

> Also, with Studio we have no of plugins that we can use. Lie for pieplines, AWS has made a plugin for Studio, and it provides you with beautiful GUI, so that you can
> watch the flow of data, and model in a better way.
