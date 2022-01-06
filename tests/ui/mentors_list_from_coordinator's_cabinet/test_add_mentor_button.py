import time
import allure
from app.ui.modules.coordinator_cabinet.mentors_list import MentorsList


def test_get_mentors_list(open_browser_chrome):
    mentors_list = MentorsList(open_browser_chrome, MentorsList.get_url)
    mentors_list.open()

    with allure.step("Add mentor"):
        mentors_list.add_mentor()

    with allure.step("Cancel"):
        mentors_list.add_mentor_cancel()
