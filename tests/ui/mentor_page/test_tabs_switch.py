import time
import allure
from app.ui.modules.mentor.mentor_page import MentorPage


def test_account_logout_is_confirmed(open_browser_chrome, logger):
    mentor_page = MentorPage(open_browser_chrome, MentorPage.authorization_url)
    mentor_page.open()
    mentor_page.should_be_authorization_page()


    with allure.step("Mentor authorization"):
        mentor_page.login_mentor_page()
        time.sleep(2)

    with allure.step("Switch to task list"):
        mentor_page.switch_to_task_list()
        time.sleep(1)

    with allure.step("Switch to archive"):
        mentor_page.switch_to_archive()
        time.sleep(1)

    with allure.step("Switch to my laborants"):
        mentor_page.switch_to_my_laborants()
        time.sleep(1)