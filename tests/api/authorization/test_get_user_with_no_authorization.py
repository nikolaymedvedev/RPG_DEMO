import allure

from app.api.helpers.users import create_random_user
from app.api.modules.authorization.steps import create_new_user, get_user_without_auth_token, \
    authorize_not_register_user, delete_user


@allure.title("Test get user with no authorization")
def test_get_user_with_no_authorization(logger):

    logger.step(step_desc="Create user")
    with allure.step("Create user"):
        new_user_data = create_random_user()
        user = create_new_user(new_user_data=new_user_data).json()

    logger.step(step_desc="Check if new user is present")
    with allure.step("Check if new user is present"):
        get_user_response = get_user_without_auth_token(username=new_user_data["username"])
        assert get_user_response.json() == "Unauthorized", "Unauthorized message is not exist"

    logger.step(step_desc="Delete user")
    with allure.step("Delete user"):
        delete_response = delete_user(new_user_data, user["id"])
        assert delete_response == "users deleted"

    logger.step(step_desc="Check if user deleted")
    with allure.step("Check if user deleted"):
        try_authorize = authorize_not_register_user(user_data=new_user_data).json()
        assert try_authorize["error"] == "user not found"
