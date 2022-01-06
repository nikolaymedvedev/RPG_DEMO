import time
import allure
from app.ui.modules.coordinator_cabinet.mentors_list import MentorsList


def test_get_mentors_list(open_browser_chrome):
    mentors_list = MentorsList(open_browser_chrome, MentorsList.get_url)
    mentors_list.open()

    with allure.step("Click page 2"):
        mentors_list.page_2()

    with allure.step("Click page 3"):
        mentors_list.page_3()

    with allure.step("Click page 1"):
        mentors_list.page_1()

