from app.ui.helpers.locators_laboratory_assistant_page import laboratoryAssistantLocators
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
        elements = self.wait_elements_located(*laboratoryAssistantLocators.LOCATOR_ALL_PERSONAL_DATA)
        result = [elem.text for elem in elements if len(elem.text) > 0]
        asserts.assert_equal(len(result), 9, "Personal information fields are missing")

    def check_availability_of_switchable_elements(self):
        elements = self.wait_elements_located(*laboratoryAssistantLocators.LOCATOR_ASSISTANT_ALL_SWITCHABLE_ELEMENTS)
        result = [elem.text for elem in elements if len(elem.text) > 0]
        asserts.assert_equal(len(result), 4, "There are no switchable fields")

    def click_enter_personal_account_button(self):
        find_element = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_ASSISTANT_PERSONAL_ACCOUNT_BUTTON)
        find_element.click()

    def click_enter_list_of_participans_button(self):
        find_element = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_ASSISTANT_LIST_OF_PARTICIPANS)
        find_element.click()

    def click_enter_hidden_menu_button(self):
        find_element = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_ASSISTANT_HIDDEN_MENU_BUTTON)
        find_element.click()

    def click_enter_notification_button(self):
        find_element = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_ASSISTANT_NOTIFICATIONS)
        find_element.click()

    def click_on_exit_button_in_the_hidden_menu(self):
        find_element = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_ASSISTANT_EXIT_BUTTON)
        find_element.click()

    def click_enter_exit_button(self):
        hidden_button = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_ASSISTANT_HIDDEN_EXIT_BUTTON)
        hidden_button.click()

    def click_on_the_exit_confirmation_button(self):
        confirmation_button = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_EXIT_CONFIRMATION_BUTTON)
        confirmation_button.click()

    def click_on_the_exit_denial_button(self):
        denial_button = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_EXIT_DENIAL_BUTTON)
        denial_button.click()

    def checking_the_exit_warning(self):
        text_warning = "Хотите выйти?"
        warning_text = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_EXIT_WARNING)
        asserts.assert_equal(warning_text.text, text_warning, "Invalid exit warning text")

    def checking_the_title_of_the_personal_data_of_the_page(self):
        title = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_ASSISTANT_PERSONAL_DATA_HEADER_OF_THE_PAGE)

    def checking_the_participants_page_title(self):
        title = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_ASSISTANT_PARTICIPANTS_HEADER_OF_THE_PAGE)

    def click_on_the_swich_button_project(self):
        button = self.wait_element_located(*laboratoryAssistantLocators.LOCATOR_ASSISTANT_BUTTON_PROJECT)
        button.click()

    def checking_the_operation_of_the_switch_button_project(self):
        list_elements = ['Проект',
                         'Дата старта',
                         'Количество участников',
                         'РМ проекта'
                         ]
        elements = self.wait_elements_located(*laboratoryAssistantLocators.LOCATOR_OF_THE_ELEMENTS_OF_THE_PROJECT_TOGGLE_BUTTON)
        all_elements = [elem.text for elem in elements if len(elem.text) > 0]
        for elem_in_list in list_elements:
            asserts.assert_in(elem_in_list, all_elements, "There are no items after clicking on the button 'project'")
