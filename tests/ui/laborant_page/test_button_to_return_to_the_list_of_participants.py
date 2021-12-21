import allure
from app.ui.modules.laborant.laborant_page import LaborantOffice
import time

def test_checking_the_hidden_menu_button_going_to_the_list_of_participants(open_browser_chrome, logger):
    lab_page = LaborantOffice(open_browser_chrome, LaborantOffice.authorization_url)
    lab_page.open()

    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()
        time.sleep(2)
    with allure.step("We are checking the operation of the go to participants page button"):
        lab_page.click_enter_list_of_participans_button()
        time.sleep(2)
        lab_page.checking_the_participants_page_title()
        time.sleep(2)
