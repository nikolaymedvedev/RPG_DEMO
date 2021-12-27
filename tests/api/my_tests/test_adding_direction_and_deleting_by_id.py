import allure
from app.api.modules.authorization.steps import get_auth_token
from app.api.modules.laborant.api_requests_directions import Directions
from configs.base_users_for_ui_and_api_tests import base_coordinator_user
from framework.utils import asserts


def ttest_adding_direction_and_deleting_by_id(logger):

    with allure.step("Authorization coordinator/get token"):
        coordinator = base_coordinator_user
        token = get_auth_token(coordinator).json()["token"]

    with allure.step("Added direction"):
        direction = Directions().add_direction(headers={"Authorization": token}
                                               )
        asserts.assert_equal(direction.status_code, 201,
                             "It is not possible to delete a direction")
        direction_id = direction.json()["id"]

    with allure.step("Delete direction by id"):
        delete_direction = Directions().delete_direction_by_id(direction_id=direction_id,
                                                               headers={"Authorization": token}
                                                               )
        asserts.assert_equal(delete_direction.text, '"directions deleted"\n',
                             "It is not possible to delete a direction by id"
                             )
