import pytest
from app.ui.modules.assistant_office.laboratory_assistant_office_page import LaboratoryAssistantOffice
import allure


def test_checking_for_the_presence_of_elements_on_the_page(open_browser_chrome, logger):
    lab_page = LaboratoryAssistantOffice(open_browser_chrome, LaboratoryAssistantOffice.authorization_url)
    lab_page.open()

    with allure.step("Авторизуемся от имени лаборанта"):
        lab_page.login_to_the_page()

    with allure.step("Проверяем наличие полей с персональными данными"):
        lab_page.check_availability_of_fields_with_personal_data()

    with allure.step("проверяем доступность переключаемых элементов"):
        lab_page.check_availability_of_switchable_elements()

    with allure.step("Проверяем доступность кнопок в скрытом меню"):
        lab_page.click_enter_personal_account_button()
        lab_page.click_enter_list_of_participans_button()
        lab_page.click_enter_hidden_menu_button()
        lab_page.click_enter_notification_button()
        lab_page.click_enter_exit_button()
