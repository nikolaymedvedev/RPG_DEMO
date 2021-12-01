from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from framework.ui.base_page import BasePage
from configs.config import get_data
from app.ui.helpers.locators_authorization_page import AuthorizationPageLocators
from framework.logger.logger import Logger
from framework.utils import asserts


class Authorization_page(BasePage):
    logger = Logger()
    authorization_url = get_data(file_name="browser_config.json")["base_url_authorization_page"]

    def should_be_authorization_page(self):
        self.should_be_authorization_url()
        asserts.assert_true(self.should_be_login_form(), "something wrong with login page")

    def should_be_authorization_url(self):
        # check if url is correct
        current_url = self.browser.current_url
        assert current_url in self.authorization_url, "not write url for login page"

    def should_be_login_form(self):
        # check if login form is presence
        try:
            self.browser.find_element(By.XPATH, "//form")
        except NoSuchElementException:
            return False
        return True

    def _clear_and_enter_text_to_field(self, locator: AuthorizationPageLocators(), text: str):
        field = self.wait_element_located(*locator)
        field.click()
        field.send_keys(Keys.BACKSPACE * 100)
        field.send_keys(text)

    def input_login(self, login: str):
        self._clear_and_enter_text_to_field(AuthorizationPageLocators.LOCATOR_LOGIN_FIELD, login)

    def input_password(self, password: str):
        self._clear_and_enter_text_to_field(AuthorizationPageLocators.LOCATOR_PASSWORD_FIELD, password)

    def click_enter_button(self):
        return self.wait_element_clickable(*AuthorizationPageLocators.LOCATOR_ENTER_BUTTON).click()

    def _required_alert_exist(self, alert_locator):
        try:
            self.wait_element_located(*alert_locator, timeout=5)
        except TimeoutException:
            return False
        return True

    def check_login_field_empty_alert(self):
        alert_exist = self._required_alert_exist(AuthorizationPageLocators.LOCATOR_ALERT_REQUIRED_FIELD_LOGIN)
        asserts.assert_true(alert_exist, "No alert 'Обязательное поле' for login field")

    def check_password_field_empty_alert(self):
        alert_exist = self._required_alert_exist(AuthorizationPageLocators.LOCATOR_ALERT_REQUIRED_FIELD_PASSWORD)
        asserts.assert_true(alert_exist, "No alert 'Обязательное поле' for password field")

    def check_alert_not_correct_login_or_password(self):
        alert_exist = self._required_alert_exist(AuthorizationPageLocators.LOCATOR_ALERT_NOT_VALID_LOGIN_OR_PASSWORD)
        asserts.assert_true(alert_exist, "No alert 'Неверные логин или пароль.'")

    def check_alert_login_length(self):
        alert_exist = self._required_alert_exist(AuthorizationPageLocators.LOCATOR_ALERT_PASSWORD_LENGTH)
        asserts.assert_true(alert_exist, "No alert 'Пароль должен содержать 12 символов' for login field")
