import allure
from app.ui.modules.assistant_office.laboratory_assistant_office_page import LaborantOffice


def test_checking_for_the_presence_of_elements_on_the_page(open_browser_chrome, logger):
    lab_page = LaborantOffice(open_browser_chrome, LaborantOffice.authorization_url)
    lab_page.open()

    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()

    with allure.step("We leave the laboratory assistant's office"):
        lab_page.click_on_exit_button_in_the_hidden_menu()
        lab_page.click_enter_exit_button()
        lab_page.click_on_the_exit_denial_button()

    with allure.step("We check the exit from the cabinet by searching for personal information fields"):
        lab_page.check_availability_of_fields_with_personal_data()
