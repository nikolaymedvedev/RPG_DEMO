import time
import allure
from app.ui.modules.mentor.mentor_page import MentorPage


def test_account_logout_is_confirmed(open_browser_chrome, logger):
    mentor_page = MentorPage(open_browser_chrome, MentorPage.authorization_url)
    mentor_page.open()
    mentor_page.should_be_authorization_page()


    with allure.step("Mentor authorization"):
        mentor_page.login_mentor_page()

    with allure.step("Find search button"):
        mentor_page.find_search_button()

    with allure.step("Find personal room button"):
        mentor_page.find_personal_room_button()
