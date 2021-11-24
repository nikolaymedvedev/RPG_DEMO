import allure

from app.api.helpers.users import create_random_user
from app.api.modules.authorization.steps import create_new_user, create_not_unique_new_user
from tests.test_data.data import username_already_exists_error_message


@allure.title("Test create user with not unique values")
def test_create_user_with_not_unique_values(logger):

    logger.step(step_desc="Create user")
    with allure.step("Create user"):
        new_user_data = create_random_user()
        create_new_user(new_user_data=new_user_data)

    logger.step(step_desc="Create not unique user")
    with allure.step("Create not unique user"):
        create_same_user_response = create_not_unique_new_user(user_data=new_user_data)
        assert create_same_user_response.json()["error"] == "username already exists",\
            username_already_exists_error_message
