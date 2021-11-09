import allure

from app.api.helpers.users import create_random_user
from app.api.moduls.authorization.steps import create_new_user, get_auth_token, get_user
from tests.test_data.data import username_already_exists_error_message


@allure.title("Test create user with valid data")
def test_create_user_with_valid_data(logger):

    logger.step(step_desc="Create user")
    with allure.step("Create user"):
        new_user_data = create_random_user()
        create_new_user(new_user_data=new_user_data)

    logger.step(step_desc="Get auth token")
    with allure.step("Get auth token"):
        auth_token = get_auth_token(user_data=new_user_data).json()["token"]

    logger.step("Check if new user is present")
    with allure.step("Check if new user is present"):
        get_user_response = get_user(username=new_user_data["username"], auth_token=auth_token)
        assert get_user_response.json()["hello_response"] == f"Hello {new_user_data['username']}!",\
            username_already_exists_error_message
