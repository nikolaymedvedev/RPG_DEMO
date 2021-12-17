from app.ui.helpers.locators_laborant_page import LaborantPageLocators
from app.ui.modules.authorization.authorization_page import Authorization_page
from configs.base_users_for_ui_and_api_tests import base_laborant_user
from framework.utils import asserts


class LaborantOffice(Authorization_page):

    ENGLISH_LEVEL = ["A", "B", "C", "1", "2", "3"]
    NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    def login_to_the_page(self, login=base_laborant_user["username"],
                          password=base_laborant_user["password"]
                          ):
        self.input_login(login)
        self.input_password(password)
        self.click_enter_button()

    def check_availability_of_fields_with_personal_data(self):
        elements = self.wait_elements_located(*LaborantPageLocators.LOCATOR_ALL_PERSONAL_DATA)
        result = [elem.text for elem in elements if len(elem.text) > 0]
        asserts.assert_equal(len(result), 9, "Personal information fields are missing")

    def check_availability_of_switchable_elements(self):
        elements = self.wait_elements_located(*LaborantPageLocators.LOCATOR_LABORANT_ALL_SWITCHABLE_ELEMENTS)
        result = [elem.text for elem in elements if len(elem.text) > 0]
        asserts.assert_equal(len(result), 4, "There are no switchable fields")

    def click_enter_personal_account_button(self):
        find_element = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_PERSONAL_ACCOUNT_BUTTON)
        find_element.click()

    def click_enter_list_of_participans_button(self):
        find_element = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_LIST_OF_PARTICIPANS)
        find_element.click()

    def click_enter_hidden_menu_button(self):
        find_element = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_HIDDEN_MENU_BUTTON)
        find_element.click()

    def click_enter_notification_button(self):
        find_element = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_NOTIFICATIONS)
        find_element.click()

    def click_on_exit_button_in_the_hidden_menu(self):
        find_element = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_EXIT_BUTTON)
        find_element.click()

    def click_enter_exit_button(self):
        hidden_button = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_HIDDEN_EXIT_BUTTON)
        hidden_button.click()

    def click_on_the_exit_confirmation_button(self):
        confirmation_button = self.wait_element_located(*LaborantPageLocators.LOCATOR_EXIT_CONFIRMATION_BUTTON)
        confirmation_button.click()

    def click_on_the_exit_denial_button(self):
        denial_button = self.wait_element_located(*LaborantPageLocators.LOCATOR_EXIT_DENIAL_BUTTON)
        denial_button.click()

    def checking_the_exit_warning(self):
        text_warning = "Хотите выйти?"
        warning_text = self.wait_element_located(*LaborantPageLocators.LOCATOR_EXIT_WARNING)
        asserts.assert_equal(warning_text.text, text_warning, "Invalid exit warning text")

    def checking_the_title_of_the_personal_data_of_the_page(self):
        self.wait_element_located(
            *LaborantPageLocators.LOCATOR_LABORANT_PERSONAL_DATA_HEADER_OF_THE_PAGE)

    def checking_the_participants_page_title(self):
        self.wait_element_located(
            *LaborantPageLocators.LOCATOR_LABORANT_PARTICIPANTS_HEADER_OF_THE_PAGE
        )

    def click_on_the_swich_button_project(self):
        button = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_BUTTON_PROJECT)
        button.click()

    def checking_the_operation_of_the_switch_button_project(self):
        list_elements = ['Проект', 'Дата старта', 'Количество участников', 'РМ проекта']
        elements = self.wait_elements_located(
            *LaborantPageLocators.LOCATOR_OF_THE_ELEMENTS_OF_THE_PROJECT_TOGGLE_BUTTON)
        all_elements = [elem.text for elem in elements if len(elem.text) > 0]
        for elem_in_list in list_elements:
            asserts.assert_in(elem_in_list, all_elements, "There are no items after clicking on the button 'project'")

    def checking_the_avatar(self):
        self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_AVATAR)

    def check_name_laborant(self):
        name = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_NAME)
        assert len(name.text) > 0

    def check_departament(self):
        departament = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_DEPARTAMENT)
        assert len(departament.text) > 0

    def check_language_level(self):
        language = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_LANGUAGE_LEVEL)
        for word in language.text:
            asserts.assert_in(word, LaborantOffice.ENGLISH_LEVEL, "Problem with language level display")

    def check_date_of_birth_format(self):
        error = "Incorrect date of birth format"
        date = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_DATE_OF_BIRTH)
        date_list = date.text.split(".")
        assert len(date_list[0]) == 2 and len(date_list[1]) == 2 and len(date_list[2]) == 4, error

    def check_telephone_format(self):
        telephone = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_TELEPHONE_FORMAT)
        telephone_new = telephone.text.replace(" ", "")
        for number in telephone_new:
            asserts.assert_in(int(number), LaborantOffice.NUMBERS, "Incorrect phone format")

    def click_on_skype_link(self):
        skype = self.wait_element_located(*LaborantPageLocators.LOCATOR_LABORANT_SKYPE_LINK)
        skype.click()

    def click_enter_number_of_participants(self):
        number = self.wait_element_located(*LaborantPageLocators.LOCATOR_NUMBER_OF_PARTICIPANTS)
        number.click()

    def check_column_name_of_participants(self):
        self.wait_element_located(*LaborantPageLocators.LOCATOR_COLUMN_NAME_OF_PARTICIPANTS)

    def checking_the_name_of_the_participants_field(self):
        self.wait_element_located(*LaborantPageLocators.LOCATOR_NAME_OF_THE_DIRECTIONS_COLUMN)

    def checking_the_names_of_project_participants(self):
        names = self.wait_elements_located(
            *LaborantPageLocators.LOCATOR_NAMES_OF_PARTICIPANTS_IN_THE_PARTICIPANTS_COLUMN
        )
        result = [i.text for i in names if len(i.text) > 0]
        asserts.assert_greater(len(result), 0, "Directions and Names are not displayed")
