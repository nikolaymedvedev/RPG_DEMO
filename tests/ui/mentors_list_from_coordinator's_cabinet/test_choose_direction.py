import time
import allure
from app.ui.modules.coordinator_cabinet.mentors_list import MentorsList


def test_get_mentors_list(open_browser_chrome):
    mentors_list = MentorsList(open_browser_chrome, MentorsList.get_url)
    mentors_list.open()

    with allure.step("Choose direction"):
        mentors_list.choose_direction()

    with allure.step("Choose DEV"):
        mentors_list.choose_direction_dev()
        mentors_list.choose_direction_dev()

    with allure.step("Choose QA"):
        mentors_list.choose_direction_qa()
        mentors_list.choose_direction_qa()

    with allure.step("Choose BA"):
        mentors_list.choose_direction_ba()
        mentors_list.choose_direction_ba()

    with allure.step("Choose UX/UI"):
        mentors_list.choose_direction_ux_ui()
        mentors_list.choose_direction_ux_ui()

    with allure.step("Choose PM"):
        mentors_list.choose_direction_pm()
        mentors_list.choose_direction_pm()

    with allure.step("Choose DevOps"):
        mentors_list.choose_direction_devops()
        mentors_list.choose_direction_devops()

    with allure.step("Choose SysAdmin"):
        mentors_list.choose_direction_sysadmin()
        mentors_list.choose_direction_sysadmin()

    with allure.step("Choose UX/UI, DevOps, SysAdmin"):
        mentors_list.choose_direction_ux_ui()
        mentors_list.choose_direction_devops()
        mentors_list.choose_direction_sysadmin()
        mentors_list.apply_direction()

    with allure.step("Choose QA"):
        mentors_list.choose_direction_ux_ui()
        mentors_list.choose_direction_devops()
        mentors_list.choose_direction_sysadmin()
        mentors_list.choose_direction_qa()
        mentors_list.apply_direction()

