import time

import allure
from app.ui.modules.assistant_office.laboratory_assistant_office_page import LaboratoryAssistantOffice


def test_checking_the_operation_of_the_switch_button_project(open_browser_chrome, logger):
    lab_page = LaboratoryAssistantOffice(open_browser_chrome, LaboratoryAssistantOffice.authorization_url)
    lab_page.open()

    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()

    with allure.step("Go to the bottom tab 'project'"):
        lab_page.click_enter_personal_account_button()
        lab_page.click_on_the_swich_button_project()

    with allure.step("Check the presence of the main fields after clicking on the bottom tab"):
        lab_page.checking_the_operation_of_the_switch_button_project()
