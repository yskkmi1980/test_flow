import prefect
from prefect import Flow, task
from prefect.storage import GitHub

import numpy

@task
def task_2(x):
    return numpy.sum(x)

with Flow("example") as flow:
    logger = prefect.context.get("logger")
    logger.info("Hello example!")
    x = 1
    y = task_2(x)

flow.storage = GitHub(repo="yskkmi1980/test_flow", path="flows/task.py")