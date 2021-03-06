import logging
from google.cloud import storage


logger = logging.getLogger()

log_handler = logging.StreamHandler()
log_handler.setLevel(logging.INFO)

logger.addHandler(log_handler)


def {{cookiecutter.project_name}}(event, context):
    logger.info("Cloud Function : {{cookiecutter.project_name}}.py, Version {}".format(__VERSION__))
