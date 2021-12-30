import allure
from app.api.modules.authorization.steps import get_auth_token, get_all_programs, create_new_program, \
    delete_program_by_id, update_program, access_to_the_program_by_id
from configs.base_users_for_ui_and_api_tests import base_coordinator_user
from framework.utils import asserts


@allure.title("Test adding an existing direction and deleting by name")
def test_adding_an_existing_direction_and_deleting_by_name(logger):

    with allure.step("Authorization coordinator/get token"):
        coordinator = base_coordinator_user
        token = get_auth_token(coordinator).json()["token"]

    with allure.step("Adding a new internship program"):
        add_program = create_new_program(headers={"Authorization": token})
        id_program = add_program.json()["id"]

    with allure.step("!!!!!!!!!!!!!!Update internship program data"):
        update = update_program(program_id=id_program,
                                headers={"Authorization": token})
        print(update.text)

    with allure.step("!!!!!!!!!!!!!!!!View the internship program using id"):
        program_by_id = access_to_the_program_by_id(program_id=id_program, headers={"Authorization": token})
        print(program_by_id.text)

    with allure.step("View all internship programs"):
        programs = get_all_programs(headers={"Authorization": token})
        asserts.assert_not_equal(len(programs.text), 0, "No internship program has been received")

    with allure.step("!!!!!!!!!!!!!!Delete a new internship program by id"):
        delete_program = delete_program_by_id(program_id=id_program,
                                              headers={"Authorization": token})
        print(delete_program.text)





