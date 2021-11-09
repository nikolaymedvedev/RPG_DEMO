import pytest
from framework.logger.logger import Logger


@pytest.fixture(scope="session")
def logger():
    logger = Logger.get_logger()
    return logger
