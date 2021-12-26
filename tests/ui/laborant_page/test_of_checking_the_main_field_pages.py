import time

from app.ui.modules.laborant.laborant_page import LaborantOffice
import allure


def test_checking_for_the_presence_of_elements_on_the_page(open_browser_chrome, logger):
    lab_page = LaborantOffice(open_browser_chrome, LaborantOffice.authorization_url)
    lab_page.open()
    time.sleep(1)
    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()
        time.sleep(1)
    with allure.step("We check the presence of fields with personal data"):
        lab_page.check_availability_of_fields_with_personal_data()
        time.sleep(1)
    with allure.step("Checking the availability of switchable elements"):
        lab_page.check_availability_of_switchable_elements()
        time.sleep(1)
    with allure.step("Check the availability of buttons in the hidden menu"):
        lab_page.click_enter_personal_account_button()
        time.sleep(1)
        lab_page.click_enter_list_of_participans_button()
        time.sleep(1)
        lab_page.click_enter_hidden_menu_button()
        time.sleep(1)
        lab_page.click_enter_notification_button()
        time.sleep(1)
        lab_page.click_on_exit_button_in_the_hidden_menu()
        time.sleep(1)
