import allure

from app.api.helpers.users import create_random_user
from app.api.moduls.authorization.steps import create_new_user, get_user_without_auth_token


@allure.title("Test get user with no authorization")
def test_get_user_with_no_authorization(logger):

    logger.step(step_desc="Create user")
    with allure.step("Create user"):
        new_user_data = create_random_user()
        create_new_user(new_user_data=new_user_data)

    logger.step(step_desc="Check if new user is present")
    with allure.step("Check if new user is present"):
        get_user_response = get_user_without_auth_token(username=new_user_data["username"])
        assert get_user_response.json() == "Unauthorized", "Unauthorized message is not exist"
