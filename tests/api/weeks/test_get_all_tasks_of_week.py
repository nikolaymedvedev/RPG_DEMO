import allure
from app.api.modules.authorization.authorization_steps import get_auth_token
from app.api.modules.programs.programs_steps import create_new_program, delete_program_by_id
from app.api.modules.tasks.tasks_steps import create_new_task, delete_new_task_by_id
from app.api.modules.weeks.weeks_steps import add_week, get_all_tasks_of_week, delete_week
from configs.base_users_for_ui_and_api_tests import base_coordinator_user


@allure.title("Test get all tasks of week")
def test_get_all_tasks_of_week(logger):

    """with allure.step("Getting a Coordinator Token"):
        coordinator = base_coordinator_user
        token = get_auth_token(coordinator).json()["token"]"""

    with allure.step("Adding a new internship program"):
        add_program = create_new_program(headers=None)
        id_program = add_program.json()["id"]

    with allure.step("Creating a new week"):
        week = add_week(week_number=1,
                        program_id=id_program,
                        headers=None)
        id_week = week.json()["id"]

    with allure.step("creating a new task"):
        new_task = create_new_task(weekID=id_week,
                                   headers=None,
                                   priority="actual",
                                   status="to_do")
        id_task = new_task.json()["id"]
        print(new_task.text)

    with allure.step("Getting all the tasks of a certain week"):
        all_tasks_on_week = get_all_tasks_of_week(week_id=id_week)
        print(all_tasks_on_week.text)



    with allure.step("Delete new certain week by id"):
        delete_w = delete_week(week_id=id_week,
                               headers=None)
        print(delete_w.text)

    with allure.step("Delete new certain program by id"):
        delete_p = delete_program_by_id(program_id=id_program,
                                        headers=None)
        print(delete_p.text)
