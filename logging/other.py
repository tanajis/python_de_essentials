import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def dummy_func():
    logger.info("This message is from other module/package")
    return 1