import allure
from app.api.modules.authorization.authorization_steps import get_auth_token
from app.api.modules.programs.programs_steps import create_new_program, delete_program_by_id
from app.api.modules.weeks.weeks_steps import add_week, get_week_by_id, update_week, delete_week
from configs.base_users_for_ui_and_api_tests import base_coordinator_user


@allure.title("Add new week, view week and update week")
def test_add_view_and_update_week(logger):

    with allure.step("Authorization coordinator/get token"):
        coordinator = base_coordinator_user
        token = get_auth_token(coordinator).json()["token"]

    with allure.step("Adding a new internship program"):
        add_program = create_new_program(headers={"Authorization": token}
                                         )
        id_program = add_program.json()["id"]

    with allure.step("Add new week"):
        week = add_week(week_number=1,
                        program_id=id_program,
                        headers={"Authorization": token}
                        )
        id_week = week.json()["id"]

    with allure.step("View a specific week by id"):
        view_week = get_week_by_id(week_id=id_week
                                   )
        print(view_week.text)

    with allure.step("Update week"):
        new_week = update_week(week_id=id_week,
                               program_id=id_program
                               )

    with allure.step("Delete new week by id"):
        delete = delete_week(week_id=id_week,
                             headers={"Authorization": token}
                             )

    with allure.step("Delete a new internship program by id"):
        delete_program = delete_program_by_id(program_id=id_program,
                                              headers={"Authorization": token}
                                              )
