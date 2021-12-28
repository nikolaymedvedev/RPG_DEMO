import pytest
from framework.logger.logger import Logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def logger():
    logger = Logger.get_logger()
    return logger


@pytest.fixture()
def open_browser_chrome(request):
    option = webdriver.ChromeOptions()
    option.headless = False
    option.add_argument("start-maximized")
    browser = webdriver.Chrome(options=option, executable_path=ChromeDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

