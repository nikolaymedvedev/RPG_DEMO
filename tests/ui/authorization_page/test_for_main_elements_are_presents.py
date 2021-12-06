import allure
from app.ui.modules.authorization.authorization_page import Authorization_page


def test_for_main_elements_are_presents(open_browser_chrome):
    auth_page = Authorization_page(open_browser_chrome, Authorization_page.authorization_url)
    auth_page.open()

    with allure.step("Checking the link button name"):
        auth_page.check_input_fields()

    with allure.step("Checking the presence of the button"):
        auth_page.check_authorization_button()

    with allure.step("Checking the presence of the link button"):
        auth_page.check_forgot_password_button()
