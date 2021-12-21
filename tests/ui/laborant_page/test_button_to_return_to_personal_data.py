import time

import allure
from app.ui.modules.laborant.laborant_page import LaborantOffice


def test_checking_the_hidden_menu_button_return_to_the_personal_account_page(open_browser_chrome, logger):
    lab_page = LaborantOffice(open_browser_chrome, LaborantOffice.authorization_url)
    lab_page.open()

    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()
        time.sleep(1)
    with allure.step("We check the operation of the back to the personal account page button"):
        lab_page.click_enter_personal_account_button()
        time.sleep(1)
        lab_page.checking_the_title_of_the_personal_data_of_the_page()
        time.sleep(1)
