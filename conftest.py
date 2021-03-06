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
    option.add_argument("--headless")
    browser = webdriver.Chrome(options=None, executable_path=ChromeDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def open_browser_firefox():
    option = webdriver.FirefoxOptions()
    option.add_argument("--headless")
    browser = webdriver.Firefox(options=None, executable_path=GeckoDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
    
    
@pytest.fixture(scope="function",
                params=[webdriver.Firefox(executable_path=GeckoDriverManager().install()),
                        webdriver.Chrome(executable_path=ChromeDriverManager().install())],
                ids=["Mazila",
                     "Chrome"]
                )
def open_browser_factory(request):
    browsers = request.param
    browsers.implicitly_wait(10)
    yield browsers
    browsers.quit()
