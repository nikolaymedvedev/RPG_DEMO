import allure

from app.ui.modules.authorization.authorization_page import Authorization_page


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

    with allure.step("Input non-valid 'Login' and valid 'Password'"):
        auth_page.input_login("nonvalid")
        auth_page.input_password("password1234")
        auth_page.click_enter_button()
        auth_page.check_alert_not_correct_login_or_password()

    with allure.step("Input valid 'Login' and non-valid 'Password'"):
        auth_page.input_login("base_mentor@andersenlab.com")
        auth_page.input_password("nonvalid")
        auth_page.click_enter_button()
        auth_page.check_alert_login_length()
