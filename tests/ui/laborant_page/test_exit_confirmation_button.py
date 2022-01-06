import allure
from app.ui.modules.laborant.laborant_page import LaborantOffice
import time


def test_checking_exit_confirmation_button(open_browser_chrome, logger):
    lab_page = LaborantOffice(open_browser_chrome, LaborantOffice.authorization_url)
    lab_page.open()
    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()

    with allure.step("We leave the laboratory assistant's office"):
        lab_page.click_on_exit_button_in_the_hidden_menu()
        lab_page.click_enter_exit_button()
        lab_page.click_on_the_exit_confirmation_button()

    with allure.step("Checking the authorization page link"):
        lab_page.check_exit_from_the_cabinet()
