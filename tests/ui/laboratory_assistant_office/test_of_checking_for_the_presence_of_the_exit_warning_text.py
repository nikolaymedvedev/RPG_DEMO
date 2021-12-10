import allure
from app.ui.modules.assistant_office.laboratory_assistant_office_page import LaboratoryAssistantOffice


def test_checking_for_the_presence_of_elements_on_the_page(open_browser_chrome, logger):
    lab_page = LaboratoryAssistantOffice(open_browser_chrome, LaboratoryAssistantOffice.authorization_url)
    lab_page.open()

    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()

    with allure.step("We are checking the text of the exit warning"):
        lab_page.clik_on_exit_button_in_the_hidden_menu()
        lab_page.click_enter_exit_button()
        lab_page.checking_the_exit_warning()
