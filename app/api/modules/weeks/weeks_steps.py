from app.api.modules.weeks.api_requests_weeks import Weeks
from framework.utils.checks import CommonCheckers


# create new week
def add_week(program_id: int, week_number: int = 1, headers: dict = None):
    week = Weeks().add_week(program_id=program_id, week_number=week_number, headers=headers)
    CommonCheckers().check_status_code_201(response=week)
    return week


# get week by id
def get_week_by_id(week_id: int):
    week = Weeks().get_week_by_id(week_id=week_id)
    CommonCheckers().check_status_code_200(response=week)
    return week


# update week
def update_week(week_id: int, program_id: int, week_number: int = 2):
    new_week = Weeks().update_week(week_id=week_id, week_number=week_number, program_id=program_id)
    CommonCheckers().check_status_code_200(response=new_week)
    return new_week


# get all tasks of week by id
def get_all_tasks_of_week(week_id: int):
    all_tasks = Weeks().get_all_tasks_of_week(week_id=week_id)
    CommonCheckers().check_status_code_200(response=all_tasks)
    return all_tasks


# get all literature of week
def get_all_literature_of_week(week_id: int):
    get_all_literature = Weeks(). get_all_literature_of_week(week_id=week_id)
    CommonCheckers().check_status_code_200(response=get_all_literature)
    return get_all_literature


# delete week by id week
def delete_week(week_id: int, headers: dict = None):
    delete = Weeks().delete_week_by_id(week_id=week_id, headers=headers)
    CommonCheckers().check_status_code_200(response=delete)
    return delete
