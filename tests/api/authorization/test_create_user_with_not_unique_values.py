import allure
from app.api.helpers.users import create_random_user
from app.api.modules.authorization.authorization_steps import create_new_user, \
    create_not_unique_new_user, delete_user, authorize_not_register_user
from tests.test_data.data import username_already_exists_error_message


@allure.title("Test create user with not unique values")
def test_create_user_with_not_unique_values(logger):

    logger.step(step_desc="Create user")
    with allure.step("Create user"):
        new_user_data = create_random_user()
        user = create_new_user(new_user_data=new_user_data).json()

    logger.step(step_desc="Create not unique user")
    with allure.step("Create not unique user"):
        create_same_user_response = create_not_unique_new_user(user_data=new_user_data)
        assert create_same_user_response.json()["error"] == "username already exists",\
            username_already_exists_error_message

    logger.step(step_desc="Delete user")
    with allure.step("Delete user"):
        delete_response = delete_user(new_user_data, user["id"])
        assert delete_response == "users deleted"

    logger.step(step_desc="Check if user deleted")
    with allure.step("Check if user deleted"):
        try_authorize = authorize_not_register_user(user_data=new_user_data).json()
        assert try_authorize["error"] == "user not found"
