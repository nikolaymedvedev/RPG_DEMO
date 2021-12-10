from app.ui.helpers.locators_authorization_page import laboratoryAssistantOfficePageLocators
from app.ui.modules.authorization.authorization_page import Authorization_page
from configs.base_users_for_ui_and_api_tests import base_laborant_user
from framework.utils import asserts


class LaboratoryAssistantOffice(Authorization_page):

    def login_to_the_page(self, login=base_laborant_user["username"],
                          password=base_laborant_user["password"]
                          ):
        self.input_login(login)
        self.input_password(password)
        self.click_enter_button()

    def check_availability_of_fields_with_personal_data(self):
        elements = self.wait_elements_located(*laboratoryAssistantOfficePageLocators.LOCATOR_ALL_PERSONAL_DATA)
        result = [elem.text for elem in elements if len(elem.text) > 0]
        asserts.assert_equal(len(result), 9, "")

    def check_availability_of_switchable_elements(self):
        elements = self.wait_elements_located(*laboratoryAssistantOfficePageLocators.LOCATOR_ASSISTANT_ALL_SWITCHABLE_LEMENTS)
        result = [elem.text for elem in elements if len(elem.text) > 0]
        asserts.assert_equal(len(result), 4, "")

    def click_enter_personal_account_button(self):
        find_element = self.wait_element_located(*laboratoryAssistantOfficePageLocators.LOCATOR_ASSISTANT_PERSONAL_ACCOUNT_BUTTON)
        find_element.click()

    def click_enter_list_of_participans_button(self):
        find_element = self.wait_element_located(*laboratoryAssistantOfficePageLocators.LOCATOR_ASSISTANT_LIST_OF_PARTICIPANS)
        find_element.click()

    def click_enter_hidden_menu_button(self):
        find_element = self.wait_element_located(*laboratoryAssistantOfficePageLocators.LOCATOR_ASSISTANT_HIDDEN_MENU_BUTTON)
        find_element.click()

    def click_enter_notification_button(self):
        find_element = self.wait_element_located(*laboratoryAssistantOfficePageLocators.LOCATOR_ASSISTANT_NOTIFICATIONS)
        find_element.click()

    def click_enter_exit_button(self):
        find_element = self.wait_element_located(*laboratoryAssistantOfficePageLocators.LOCATOR_ASSISTANT_EXIT_BUTTON)
        find_element.click()
