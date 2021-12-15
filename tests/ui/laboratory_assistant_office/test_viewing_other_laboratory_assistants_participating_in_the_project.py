import allure
from app.ui.modules.assistant_office.laboratory_assistant_office_page import LaborantOffice


def test_checking_the_operation_of_the_switch_button_project(open_browser_chrome, logger):
    lab_page = LaborantOffice(open_browser_chrome, LaborantOffice.authorization_url)
    lab_page.open()

    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()

    with allure.step("Go to the project participants page"):
        lab_page.click_on_the_swich_button_project()
        lab_page.click_enter_number_of_participants()

    with allure.step("Checking the correctness of the column name 'Name'"):
        lab_page.check_column_name_of_participants()

    with allure.step("Checking the correctness of the column name 'Directions'"):
        lab_page.checking_the_name_of_the_participants_field()

    with allure.step("We check that the received list of directions and names is not empty"):
        lab_page.checking_the_names_of_project_participants()
