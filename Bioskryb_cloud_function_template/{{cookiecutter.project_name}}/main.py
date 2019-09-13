import logging

from google.cloud import storage

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

log_handler = logging.StreamHandler()
log_handler.setLevel(logging.DEBUG)

logger.addHandler(log_handler)

__VERSION__="0.1.0"


