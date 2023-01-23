import logging
import sys

logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout,
                    format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("some info")
    logger.warning("some warning")
    logger.error("some error")