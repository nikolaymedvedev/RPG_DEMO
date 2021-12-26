import allure
from app.ui.modules.laborant.laborant_page import LaborantOffice
import time
from framework.utils import asserts


def test_checking_exit_confirmation_button(open_browser_chrome, logger):
    lab_page = LaborantOffice(open_browser_chrome, LaborantOffice.authorization_url)
    lab_page.open()
    time.sleep(1)
    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()
        time.sleep(1)
    with allure.step("We leave the laboratory assistant's office"):
        lab_page.click_on_exit_button_in_the_hidden_menu()
        time.sleep(1)
        lab_page.click_enter_exit_button()
        time.sleep(1)
        lab_page.click_on_the_exit_confirmation_button()
        time.sleep(1)
    with allure.step("Checking the authorization page link"):
        asserts.assert_true(lab_page.wait_for_url(LaborantOffice.authorization_url),
                            "Not correct url opened")
        time.sleep(1)
