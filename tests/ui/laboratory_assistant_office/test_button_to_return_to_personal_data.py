import allure
from app.ui.modules.assistant_office.laboratory_assistant_office_page import LaboratoryAssistantOffice


def test_checking_the_hidden_menu_button_return_to_the_personal_account_page(open_browser_chrome, logger):
    lab_page = LaboratoryAssistantOffice(open_browser_chrome, LaboratoryAssistantOffice.authorization_url)
    lab_page.open()

    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()

    with allure.step("We check the operation of the back to the personal account page button"):
        lab_page.click_enter_personal_account_button()
        lab_page.checking_the_title_of_the_personal_data_of_the_page()
