import time
from selenium import webdriver
import allure
from app.ui.modules.coordinator_cabinet.mentors_list import MentorsList


def test_get_mentors_list(open_browser_chrome):
    mentors_list = MentorsList(open_browser_chrome, MentorsList.get_url)
    mentors_list.open()

    with allure.step("Find My profile button"):
        mentors_list.my_profile()

    with allure.step("Find quit button"):
        mentors_list.quit_button()

    with allure.step("Cancel quit"):
        mentors_list.quit_button_no()
        webdriver.Chrome.refresh(open_browser_chrome)

    with allure.step("Find My profile button"):
        mentors_list.my_profile()

    with allure.step("Find quit button"):
        mentors_list.quit_button()

    with allure.step("Сonfirm quit"):
        mentors_list.quit_button_yes()
