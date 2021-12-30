import allure
from app.ui.modules.authorization.authorization_page import Authorization_page


def test_button_forgot_password(open_browser_chrome, logger):
    auth_page = Authorization_page(open_browser_chrome, Authorization_page.authorization_url)
    auth_page.open()

    with allure.step("Checking the link button name"):
        auth_page.check_text_in_forgot_password_button()

    with allure.step("Checking the message header after clicking on the link button"):
        auth_page.click_on_link_button()
        auth_page.check_heading_after_click_on_forgot_password_button()

    with allure.step("Checking the message field after clicking on the link button"):
        auth_page.check_field_after_click_on_forgot_password_button()

    with allure.step("Checking that the field is required"):
        auth_page.click_button_send_email_button()
        auth_page.checking_the_required_field()

    with allure.step("Checking sending invalid mail"):
        auth_page.check_mail_input_field()
        auth_page.input_text_in_mail_field("invalid")
        auth_page.click_button_send_email_button()
        auth_page.checking_sending_invalid_mail()

    with allure.step("Checking that the window 'forgot password' has closed"):
        auth_page.close_window_forgot_password()
        auth_page.check_return_on_authorization_windows()
