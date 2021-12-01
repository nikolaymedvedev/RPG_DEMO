import allure

from app.ui.modules.authorization.authorization_page import Authorization_page
import pytest
from configs.base_users_for_ui_and_api_tests import base_mentor_user, base_laborant_user
import framework.utils.asserts as asserts
from configs.config import get_data


mentor_cabinet_url = get_data(file_name="browser_config.json")["base_url_mentor_cabinet_page"]
laborant_cabinet_url = get_data(file_name="browser_config.json")["base_url_laborant_cabinet_page"]

# TODO wait for coordinator page and add to test
coordinator_cabinet_url = get_data(file_name="browser_config.json")["base_url_coordinator_cabinet_page"]


@pytest.mark.parametrize("role, username, password, url", [
    ("mentor", base_mentor_user["username"], base_mentor_user["password"], mentor_cabinet_url),
    ("laborant", base_laborant_user["username"], base_laborant_user["password"], laborant_cabinet_url)
])
def test_success_enter_to_cabinet(open_browser_chrome, logger, role, url, username, password):
    auth_page = Authorization_page(open_browser_chrome, Authorization_page.authorization_url)
    auth_page.open()
    auth_page.should_be_authorization_page()

    with allure.step(f"Enter valid {role} credentials"):
        auth_page.input_login(username)
        auth_page.input_password(password)
        auth_page.click_enter_button()

    with allure.step(f"Check if enter to {role} cabinet was successful"):
        asserts.assert_true(auth_page.wait_for_url(url), "Not correct url opened")
