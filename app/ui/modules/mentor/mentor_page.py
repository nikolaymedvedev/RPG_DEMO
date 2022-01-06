from app.ui.helpers.locators_mentor_page import MentorPageLocators
from app.ui.modules.authorization.authorization_page import Authorization_page
from configs.base_users_for_ui_and_api_tests import base_mentor_user
from framework.utils import asserts
from selenium.webdriver.common.by import By


class MentorPage(Authorization_page):

    def login_mentor_page(self, login=base_mentor_user["username"],
                          password=base_mentor_user["password"]
                          ):
        self.input_login(login)
        self.input_password(password)
        self.click_enter_button()

    def find_mentor_name(self):
        mentor_name = self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_NAME)
        assert len(mentor_name.text) > 0, "Mentor name not found"

    def find_mentor_photo(self):
        mentor_photo = self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_PHOTO)

    def find_mentor_location(self):
        mentor_location = self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_LOCATION)

    def find_mentor_phone_number(self):
        mentor_phone_number = self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_PHONE_NUMBER)

    def find_mentor_email(self):
        mentor_email = self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_EMAIL)

    def find_mentor_skype(self):
        mentor_skype = self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_SKYPE)

    def find_my_profile_button(self):
        my_profile_button = self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_MY_PROFILE).click()

    def find_quit_button(self):
        quit_button = self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_QUIT).click()

    def select_no(self):
        quit_no_button = self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_QUIT_NO).click()

    def select_yes(self):
        quit_yes_button = self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_QUIT_YES).click()

    def find_search_button(self):
        search_button = self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_SEARCH).click()

    def find_personal_room_button(self):
        personal_room_button = self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_PERSONAL_ROOM).click()

    def switch_to_my_laborants(self):
        my_laborants = self.wait_element_located(*MentorPageLocators.LOCATOR_LABORANTS).click()

    def switch_to_task_list(self):
        task_list = self.wait_element_located(*MentorPageLocators.LOCATOR_TASK_LIST).click()

    def switch_to_archive(self):
        archive = self.wait_element_located(*MentorPageLocators.LOCATOR_ARCHIVE).click()

    def first_laborant_page(self):
        first_laborant = self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT).click()

    def switch_to_project(self):
        laborant_project = self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_PROJECT).click()

    def first_team_members(self):
        laborant_first_team = self.wait_element_located(
            *MentorPageLocators.LOCATOR_FIRST_LABORANT_PROJECT_ONE_TEAM).click()

    def close_members_list(self):
        close_members_list = self.wait_element_located(
            *MentorPageLocators.LOCATOR_FIRST_LABORANT_PROJECT_ONE_TEAM_CLOSE) .click()

    def switch_to_timesheets(self):
        laborant_timesheets = self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_TIMESHEETS).click()

    def switch_to_tasks(self):
        laborant_tasks = self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_TASKS).click()

    def switch_to_info(self):
        laborant_info = self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO).click()

    def add_feedback(self):
        laborant_feedback = self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO_FEEDBACK).click()

    def find_feedback_area(self):
        laborant_feedback = self.wait_element_located(
            *MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO_FEEDBACK_TEXTAREA).send_keys("Добавлять не будем, "
                                                                                         "просто проверяем, что работает")
    def cancel_feedback_adding(self):
        laborant_feedback_cancel = self.wait_element_located(
            *MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO_FEEDBACK_CANCEL).click()

