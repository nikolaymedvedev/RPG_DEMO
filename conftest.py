import multiprocessing

import pytest
from framework.logger.logger import Logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def logger():
    logger = Logger.get_logger()
    return logger


@pytest.fixture()
def open_browser_chrome(scope="function"):
    option = webdriver.ChromeOptions()
    option.headless = False
    browser = webdriver.Chrome(options=None, executable_path=ChromeDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def open_browser_firefox():
    option = webdriver.FirefoxOptions()
    option.headless = True
    option.set_capability()
    browser = webdriver.Firefox(options=None, executable_path=GeckoDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
