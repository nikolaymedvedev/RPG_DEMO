import allure

from app.api.helpers.users import create_random_user
from app.api.modules.authorization.steps import create_new_user, get_auth_token, get_user, \
    authorize_not_register_user, delete_user
from tests.test_data.data import username_already_exists_error_message


@allure.title("Test create user with valid data")
def test_create_user_with_valid_data(logger):

    logger.step(step_desc="Create user")
    with allure.step("Create user"):
        new_user_data = create_random_user()
        user = create_new_user(new_user_data=new_user_data).json()

    logger.step(step_desc="Get auth token")
    with allure.step("Get auth token"):
        auth_token = get_auth_token(user_data=new_user_data).json()["token"]

    logger.step("Check if new user is present")
    with allure.step("Check if new user is present"):
        get_user_response = get_user(username=new_user_data["username"], auth_token=auth_token)
        assert get_user_response.json()["hello_response"] == f"Hello {new_user_data['username']}!",\
            username_already_exists_error_message

    logger.step(step_desc="Delete user")
    with allure.step("Delete user"):
        delete_response = delete_user(new_user_data, user["id"])
        assert delete_response == "users deleted"

    logger.step(step_desc="Check if user deleted")
    with allure.step("Check if user deleted"):
        try_authorize = authorize_not_register_user(user_data=new_user_data).json()
        assert try_authorize["error"] == "user not found"
