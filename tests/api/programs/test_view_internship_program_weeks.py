import allure
from app.api.modules.authorization.authorization_steps import get_auth_token
from app.api.modules.programs.programs_steps import create_new_program, get_all_weeks_of_program, \
    get_week_by_program_id_and_number, delete_program_by_id
from app.api.modules.weeks.weeks_steps import delete_week, add_week
from configs.base_users_for_ui_and_api_tests import base_coordinator_user


@allure.title("View all weeks of a program and a specific week of a specific program")
def test_view_internship_program_weeks(logger):
    # Pre_condition step
    with allure.step("Authorization coordinator/get token"):
        coordinator = base_coordinator_user
        token = get_auth_token(coordinator).json()["token"]
    # Pre_condition step
    with allure.step("Adding a new internship program"):
        add_program = create_new_program(headers={"Authorization": token})
        id_program = add_program.json()["id"]
    # The_main step
    with allure.step("Adding a new week"):
        week = add_week(program_id=id_program,
                        headers={"Authorization": token})
        id_week = week.json()["id"]
        print("Добавляем неделю", week.text)
    # The_main step
    with allure.step("View all weeks of the program"):
        all_weeks = get_all_weeks_of_program(program_id=id_program)
        print("Смотреть все недели на программе", all_weeks.text)
    # The_main step
    with allure.step("View a specific week of a specific program"):
        certain_week = get_week_by_program_id_and_number(program_id=id_program,
                                                         week_number=1)
        print("Посмотреть определенную неделю определенной задачи", certain_week.text)
    # Post_condition step
    with allure.step("Deleting the created week"):
        delete = delete_week(week_id=id_week,
                             headers={"Authorization": token})
        print("Удалить неделю", delete.text)
    # Post_condition step
    with allure.step("Delete the created program"):
        delete_program = delete_program_by_id(program_id=id_program,
                                              headers={"Authorization": token})
        print("Удалить программу:", delete_program.text)
