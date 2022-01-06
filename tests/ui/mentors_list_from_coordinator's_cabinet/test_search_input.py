import allure
from app.ui.modules.coordinator_cabinet.mentors_list import MentorsList


def test_get_mentors_list(open_browser_chrome):
    mentors_list = MentorsList(open_browser_chrome, MentorsList.get_url)
    mentors_list.open()

    with allure.step("Check search button"):
        mentors_list.check_search()
