import allure

from app.api.helpers.users import create_random_user
from app.api.modules.authorization.steps import create_new_user, get_auth_token, get_user, delete_user


def test_create_user_with_valid_data(logger):

    with allure.step("Create user"):
        new_user = create_random_user()
        user_registration = create_new_user(new_user).json()

    with allure.step("Get token"):
        user_authorization = get_auth_token(new_user).json()
        token = user_authorization['token']

    with allure.step("user hello"):
        hello = get_user(user_registration["username"], token)
        assert hello.json()["hello_response"] == f"Hello {user_registration['username']}!",\
            "user not found"

    with allure.step("delete"):
        del_user = delete_user(new_user, user_authorization["id"])
        assert del_user == "users deleted"
