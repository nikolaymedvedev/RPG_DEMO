import allure
from app.ui.modules.laborant.laborant_page import LaborantOffice


def test_checking_the_participants_page_title(open_browser_chrome, logger):
    lab_page = LaborantOffice(open_browser_chrome, LaborantOffice.authorization_url)
    lab_page.open()

    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()

    with allure.step("We are checking the operation of the go to participants page button"):
        lab_page.click_enter_list_of_participans_button()
        lab_page.checking_the_participants_page_title()
