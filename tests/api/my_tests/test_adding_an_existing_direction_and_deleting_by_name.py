import allure
from app.api.modules.authorization.steps import get_auth_token
from app.api.modules.laborant.api_requests_directions import Directions
from configs.base_users_for_ui_and_api_tests import base_coordinator_user
from framework.utils import asserts


def test_adding_an_existing_direction_and_deleting_by_name(logger):

    with allure.step("Authorization coordinator/get token"):
        coordinator = base_coordinator_user
        token = get_auth_token(coordinator).json()["token"]

    with allure.step("Added direction"):
        direction = Directions().add_direction(headers={"Authorization": token}
                                               )
        asserts.assert_equal(direction.status_code, 201,
                             "It is not possible to delete a direction")
        direction_name = direction.json()["name"]

    with allure.step("Creating an existing direction"):
        direction = Directions().add_direction(direction_name=direction_name,
                                               headers={"Authorization": token})
        asserts.assert_equal(direction.json()["error"],
                             "internship direction with such name already exists",
                             "Successful creation of a duplicate of the internship direction")

    with allure.step("Delete direction by name"):
        delete_direction = Directions().delete_direction_by_name(direction_name=direction_name,
                                                                 headers={"Authorization": token}
                                                                 )
        asserts.assert_equal(delete_direction.text, '"directions deleted"\n',
                             "It is not possible to delete a direction by name"
                             )