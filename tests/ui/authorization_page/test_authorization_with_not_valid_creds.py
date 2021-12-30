import allure
from app.ui.modules.authorization.authorization_page import Authorization_page
from configs.base_users_for_ui_and_api_tests import base_laborant_user


def test_authorization_with_not_valid_creds(open_browser_chrome, logger):
    auth_page = Authorization_page(open_browser_chrome, Authorization_page.authorization_url)
    auth_page.open()
    auth_page.should_be_authorization_page()

    with allure.step("Input empty values into password and login fields"):
        auth_page.input_login("")
        auth_page.input_password("")
        auth_page.click_enter_button()
        auth_page.check_login_field_empty_alert()
        auth_page.check_password_field_empty_alert()

    with allure.step("Input non-valid 'Login'"):
        auth_page.input_login("nonvalidlogin@mail.com")
        auth_page.input_password(base_laborant_user["password"])
        auth_page.click_enter_button()
        auth_page.check_alert_not_correct_login()
        auth_page.update_authorization_page()

    with allure.step("Input non-valid 'password'"):
        auth_page.input_login(base_laborant_user["username"])
        auth_page.input_password("invalidpassw")
        auth_page.click_enter_button()
        auth_page.check_alert_not_correct_password()
