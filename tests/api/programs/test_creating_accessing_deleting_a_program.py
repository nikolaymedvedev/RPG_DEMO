import allure
from app.api.modules.authorization.authorization_steps import get_auth_token
from app.api.modules.programs.programs_steps import create_new_program, update_program, access_to_the_program_by_id, \
    get_all_programs, delete_program_by_id
from configs.base_users_for_ui_and_api_tests import base_coordinator_user
from framework.utils import asserts


@allure.title("Add new program, update program, view the program by id and delete program by id")
def test_add_update_view_the_program_and_delete_by_id(logger):

    with allure.step("Authorization coordinator/get token"):
        coordinator = base_coordinator_user
        token = get_auth_token(coordinator).json()["token"]

    with allure.step("Adding a new internship program"):
        add_program = create_new_program(headers={"Authorization": token})
        id_program = add_program.json()["id"]

    with allure.step("Update internship program data"):
        update_program(program_id=id_program,
                       headers={"Authorization": token})

    with allure.step("View the internship program using id"):
        access_to_the_program_by_id(program_id=id_program,
                                    headers={"Authorization": token})

    with allure.step("View all internship programs"):
        programs = get_all_programs(headers={"Authorization": token})
        asserts.assert_not_equal(len(programs.text), 0, "No internship program has been received")

    with allure.step("Delete a new internship program by id"):
        delete_program_by_id(program_id=id_program,
                             headers={"Authorization": token})
