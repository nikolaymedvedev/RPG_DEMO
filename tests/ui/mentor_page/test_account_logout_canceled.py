import allure
from app.ui.modules.mentor.mentor_page import MentorPage


def test_account_logout_canceled(open_browser_chrome, logger):
    mentor_page = MentorPage(open_browser_chrome, MentorPage.authorization_url)
    mentor_page.open()
    mentor_page.should_be_authorization_page()

    with allure.step("Mentor authorization"):
        mentor_page.login_mentor_page()

    with allure.step("Find my profile button"):
        mentor_page.find_my_profile_button()

    with allure.step("Find quit button"):
        mentor_page.find_quit_button()

    with allure.step("Select 'No'"):
        mentor_page.select_no()

