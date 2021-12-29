import allure
from app.api.modules.authorization.steps import get_auth_token, create_invalid_direction
from configs.base_users_for_ui_and_api_tests import base_coordinator_user


@allure.title("Added invalid direction")
def test_added_invalid_direction(logger):

    with allure.step("Authorization coordinator/get token"):
        coordinator = base_coordinator_user
        token = get_auth_token(coordinator).json()["token"]

    with allure.step("Added invalid direction"):
        create_invalid_direction(direction_name="@&!**!!&&@@!",
                                 headers={"Authorization": token}
                                 )
