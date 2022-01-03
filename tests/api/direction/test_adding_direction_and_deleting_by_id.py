import allure
from app.api.modules.authorization.authorization_steps import get_auth_token
from app.api.modules.directions.directions_steps import create_direction, delete_direction_by_id
from configs.base_users_for_ui_and_api_tests import base_coordinator_user
from framework.utils import asserts


@allure.title("Test adding direction and deleting by id")
def test_adding_direction_and_deleting_by_id(logger):

    with allure.step("Authorization coordinator/get token"):
        coordinator = base_coordinator_user
        token = get_auth_token(coordinator).json()["token"]

    with allure.step("Added direction"):
        direction = create_direction(headers={"Authorization": token})
        direction_id = direction.json()["id"]

    with allure.step("Delete direction by id"):
        delete_direction = delete_direction_by_id(direction_id=direction_id,
                                                  headers={"Authorization": token}
                                                  )
        asserts.assert_equal(delete_direction.text, '"directions deleted"\n',
                             "It is not possible to delete a direction by id"
                             )
