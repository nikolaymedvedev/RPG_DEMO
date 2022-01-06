import allure
from app.ui.modules.mentor.mentor_page import MentorPage


def test_check_mentor_info(open_browser_chrome, logger):
    mentor_page = MentorPage(open_browser_chrome, MentorPage.authorization_url)
    mentor_page.open()
    mentor_page.should_be_authorization_page()

    with allure.step("Mentor authorization"):
        mentor_page.login_mentor_page()

    with allure.step("Find mentor's name"):
        mentor_page.find_mentor_name()

    with allure.step("Find mentor's photo"):
        mentor_page.find_mentor_photo()

    with allure.step("Find mentor's location"):
        mentor_page.find_mentor_location()

    with allure.step("Find mentor's phone number"):
        mentor_page.find_mentor_phone_number()

    with allure.step("Find mentor's E-mail"):
        mentor_page.find_mentor_email()

    with allure.step("Find mentor's Skype"):
        mentor_page.find_mentor_skype()

