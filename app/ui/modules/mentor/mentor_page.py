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
        self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_PHOTO)

    def find_mentor_location(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_LOCATION)

    def find_mentor_phone_number(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_PHONE_NUMBER)

    def find_mentor_email(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_EMAIL)

    def find_mentor_skype(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_SKYPE)

    def find_my_profile_button(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_MY_PROFILE).click()

    def find_quit_button(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_QUIT).click()

    def select_no(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_QUIT_NO).click()

    def select_yes(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_QUIT_YES).click()

    def find_search_button(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_SEARCH).click()

    def find_personal_room_button(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_PERSONAL_ROOM).click()

    def switch_to_my_laborants(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_LABORANTS).click()

    def switch_to_task_list(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_TASK_LIST).click()

    def switch_to_archive(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_ARCHIVE).click()

    def first_laborant_page(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT).click()

    def switch_to_project(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_PROJECT).click()

    def first_team_members(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_PROJECT_ONE_TEAM).click()

    def close_members_list(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_PROJECT_ONE_TEAM_CLOSE).click()

    def switch_to_timesheets(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_TIMESHEETS).click()

    def switch_to_tasks(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_TASKS).click()

    def switch_to_info(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO).click()

    def add_feedback(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO_FEEDBACK).click()

    def find_feedback_area(self):
        self.wait_element_located(
            *MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO_FEEDBACK_TEXTAREA).send_keys("Фидбэк")

    def cancel_feedback_adding(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO_FEEDBACK_CANCEL).click()
        self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_PHOTO)

    def find_mentor_location(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_LOCATION)

    def find_mentor_phone_number(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_PHONE_NUMBER)

    def find_mentor_email(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_EMAIL)

    def find_mentor_skype(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_MENTOR_SKYPE)

    def find_my_profile_button(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_MY_PROFILE).click()

    def find_quit_button(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_QUIT).click()

    def select_no(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_QUIT_NO).click()

    def select_yes(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_QUIT_YES).click()

    def find_search_button(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_SEARCH).click()

    def find_personal_room_button(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_BUTTON_PERSONAL_ROOM).click()

    def switch_to_my_laborants(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_LABORANTS).click()

    def switch_to_task_list(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_TASK_LIST).click()

    def switch_to_archive(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_ARCHIVE).click()

    def first_laborant_page(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT).click()

    def switch_to_project(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_PROJECT).click()

    def first_team_members(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_PROJECT_ONE_TEAM).click()

    def close_members_list(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_PROJECT_ONE_TEAM_CLOSE).click()

    def switch_to_timesheets(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_TIMESHEETS).click()

    def switch_to_tasks(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_TASKS).click()

    def switch_to_info(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO).click()

    def add_feedback(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO_FEEDBACK).click()

    def find_feedback_area(self):
        self.wait_element_located(
            *MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO_FEEDBACK_TEXTAREA).send_keys("Добавлять не будем, "
                                                                                         "просто проверяем, что работает")
    def cancel_feedback_adding(self):
        self.wait_element_located(*MentorPageLocators.LOCATOR_FIRST_LABORANT_INFO_FEEDBACK_CANCEL).click()
