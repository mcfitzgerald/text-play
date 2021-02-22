import logging
logger = logging.getLogger(__name__)

logging.debug('This message should go to the log file')

print(__name__)

def undef():
    try:
        run_my_stuff()
    except:
        logging.exception('got exception on main handler')
        raise
