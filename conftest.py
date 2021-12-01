import pytest
from framework.logger.logger import Logger
from selenium import webdriver


@pytest.fixture(scope="session")
def logger():
    logger = Logger.get_logger()
    return logger


@pytest.fixture()
def open_browser_chrome():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
