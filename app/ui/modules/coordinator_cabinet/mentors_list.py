from app.ui.helpers.locators_mentors_list_from_coordinator_cabinet import MentorsListLocators
from selenium import webdriver
from configs.config import get_data
from framework.ui.base_page import BasePage


class MentorsList(BasePage):

    get_url = get_data(file_name="browser_config.json")["base_url_coordinator_cabinet_mentors_list"]

    def check_search(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_SEARCH_INPUT).send_keys("Анастасия")

    def my_profile(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_MY_PROFILE).click()

    def quit_button(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_QUIT_BUTTON).click()

    def quit_button_no(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_QUIT_BUTTON_NO).click()

    def quit_button_yes(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_QUIT_BUTTON_YES).click()

    def add_mentor(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_ADD_MENTOR_BUTTON).click()

    def add_mentor_cancel(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_ADD_MENTOR_BUTTON_CANCEL).click()

    def choose_direction(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_DIRECTIONS_DROPDOWN).click()

    def choose_direction_dev(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_DIRECTIONS_DEV).click()

    def choose_direction_qa(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_DIRECTIONS_QA).click()

    def choose_direction_ba(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_DIRECTIONS_BA).click()

    def choose_direction_ux_ui(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_DIRECTIONS_UX_UI).click()

    def choose_direction_pm(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_DIRECTIONS_PM).click()

    def choose_direction_devops(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_DIRECTIONS_DEVOPS).click()

    def choose_direction_sysadmin(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_DIRECTIONS_SYSADMIN).click()

    def apply_direction(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_APPLY_BUTTON).click()

    def page_1(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_PAGE_1).click()

    def page_2(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_PAGE_2).click()

    def page_3(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_PAGE_3).click()

    def next_page(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_PAGE_NEXT).click()

    def previous_page(self):
        self.wait_element_located(*MentorsListLocators.LOCATOR_PAGE_PREVIOUS).click()
