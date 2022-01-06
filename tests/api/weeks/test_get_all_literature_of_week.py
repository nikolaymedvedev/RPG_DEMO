import allure
from app.api.modules.authorization.authorization_steps import get_auth_token
from app.api.modules.literature.literature_steps import add_literature, delete_literature
from app.api.modules.programs.programs_steps import create_new_program, delete_program_by_id
from app.api.modules.weeks.weeks_steps import add_week, get_all_literature_of_week, delete_week
from configs.base_users_for_ui_and_api_tests import base_coordinator_user
from framework.utils import asserts


@allure.title("Test get all literature of week")
def test_get_all_literature_of_week(logger):

    """with allure.step("Getting a Coordinator Token"):
        coordinator = base_coordinator_user
        token = get_auth_token(coordinator).json()["token"]"""

    with allure.step("Adding a new internship program"):
        add_program = create_new_program(headers=None)
        id_program = add_program.json()["id"]

    with allure.step("Creating a new week"):
        week = add_week(program_id=id_program,
                        headers=None
                        )
        id_week = week.json()["id"]

    with allure.step("Creating a new literature"):
        literature = add_literature(week_id=id_week)
        id_literature = literature.json()["id"]
        print(literature.text)

    with allure.step("view all literature of week"):
        all_literature_on_week = get_all_literature_of_week(week_id=id_week)
        asserts.assert_greater(len(all_literature_on_week.text), 0, "The literature has not been created")

    with allure.step("Delete literature"):
        delete_l = delete_literature(literature_id=id_literature)
        print(delete_l.text)

    with allure.step("Delete week"):
        delete_w = delete_week(week_id=id_week,
                               headers=None
                               )
        print(delete_w.text)

    with allure.step("Delete program"):
        delete_p = delete_program_by_id(program_id=id_program,
                                        headers=None
                                        )
        print(delete_p.text)
