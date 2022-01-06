import allure
from app.ui.modules.mentor.mentor_page import MentorPage


def test_account_logout_is_confirmed(open_browser_chrome, logger):
    mentor_page = MentorPage(open_browser_chrome, MentorPage.authorization_url)
    mentor_page.open()
    mentor_page.should_be_authorization_page()

    with allure.step("Mentor authorization"):
        mentor_page.login_mentor_page()

    with allure.step("Get to the laborant's page"):
        mentor_page.first_laborant_page()

    with allure.step("Switch to project"):
        mentor_page.switch_to_project()

    with allure.step("Show the first project team"):
        mentor_page.first_team_members()

    with allure.step("Close members list"):
        mentor_page.close_members_list()

    with allure.step("Switch to Timesheets"):
        mentor_page.switch_to_timesheets()

    with allure.step("Switch to tasks"):
        mentor_page.switch_to_tasks()

    with allure.step("Switch to info"):
        mentor_page.switch_to_info()

    with allure.step("Add feedback"):
        mentor_page.add_feedback()

    with allure.step("Find feedback area"):
        mentor_page.find_feedback_area()

    with allure.step("Cancel adding feedback"):
        mentor_page.cancel_feedback_adding()

    with allure.step("Back to the main page"):
        mentor_page.find_personal_room_button()

