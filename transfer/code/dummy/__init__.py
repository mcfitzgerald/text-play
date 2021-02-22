import logging
from dummy import bork

logger = logging.getLogger("dummy")
#if not logger.handlers:  # To ensure reload() doesn't add another one
#   logger.addHandler(logging.NullHandler())
