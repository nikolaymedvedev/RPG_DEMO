import allure
from app.api.helpers.laborants import get_random_direction_name
from app.api.modules.authorization.steps import get_auth_token
from app.api.modules.laborant.api_requests_directions import Directions
from configs.base_users_for_ui_and_api_tests import base_coordinator_user
from framework.utils import asserts


@allure.title("Test checking the direction update")
def test_update_direction(logger):

    random_direction_name = get_random_direction_name()

    with allure.step("Authorization coordinator/get token"):
        coordinator = base_coordinator_user
        token = get_auth_token(coordinator).json()["token"]

    with allure.step("Added direction"):
        direction = Directions().add_direction(headers={"Authorization": token})
        asserts.assert_equal(direction.status_code, 201, "It is not possible to delete a direction")
        direction_id = direction.json()["id"]

    with allure.step("Updating the direction"):
        update_direction = Directions().update_direction(direction_id=direction_id,
                                                         new_direction_name=random_direction_name,
                                                         headers={"Authorization": token}
                                                         )
        asserts.assert_equal(update_direction.text, '"direction updated"\n', "Failed to update direction")

    with allure.step("Delete direction by random name"):
        delete_direction = Directions().delete_direction_by_name(direction_name=random_direction_name,
                                                                 headers={"Authorization": token}
                                                                 )
        asserts.assert_equal(delete_direction.text, '"directions deleted"\n',
                             "It is not possible to delete a direction by id"
                             )
