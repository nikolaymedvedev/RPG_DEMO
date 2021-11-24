from selenium.common.exceptions import NoSuchElementException
from framework.ui.base_page import BasePage
from configs.config import get_data
from app.ui.helpers.locators_authorization_page import AuthorizationPageLocators


class Authorization_page(BasePage):

    authorization_url = get_data(file_name="browser_config.json")["base_url_authorization_page"]

    def should_be_authorization_page(self):
        self.should_be_authorization_url()
        assert self.should_be_login_form() is True, "something wrong with login page"

    def should_be_authorization_url(self):
        # check if url is correct
        current_url = self.browser.current_url
        assert current_url in self.authorization_url, "not write url for login page"

    def should_be_login_form(self):
        # check if login form is presence
        try:
            self.browser.find_element_by_xpath("//form")
        except NoSuchElementException:
            return False
        return True

    def input_login(self, login: str):
        login_field = self.wait_element_clickable(*AuthorizationPageLocators.LOCATOR_LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(login)

    def input_password(self, password: str):
        password_field = self.wait_element_clickable(*AuthorizationPageLocators.LOCATOR_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)

    def click_enter_button(self):
        self.wait_element_clickable(*AuthorizationPageLocators.LOCATOR_ENTER_BUTTON).click()
