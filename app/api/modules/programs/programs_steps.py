from app.api.modules.programs.api_requests_programs import Programs
from app.api.modules.weeks.api_requests_weeks import Weeks
from framework.utils.checks import CommonCheckers


# we are reviewing all internship programs
def get_all_programs(headers: dict = None):
    programs = Programs().get_all_programs(headers=headers)
    CommonCheckers().check_status_code_200(response=programs)
    return programs


# view the internship program by id
def access_to_the_program_by_id(program_id: int, headers: dict = None):
    program = Programs().get_program_by_id(program_id=program_id, headers=headers)
    CommonCheckers().check_status_code_200(response=program)
    return program


# adding a new internship program
def create_new_program(program_name: str = None, duration: int = None, testsQty: int = None, headers: dict = None):
    program = Programs().add_program(program_name=program_name, duration=duration, testsQty=testsQty, headers=headers)
    CommonCheckers().check_status_code_201(response=program)
    return program


# delete program by id
def delete_program_by_id(program_id: int, headers: dict = None):
    delete = Programs().delete_program_by_id(program_id=program_id, headers=headers)
    CommonCheckers().check_status_code_200(response=delete)
    return delete


# updating internship program data
def update_program(program_id: int, new_program_name: str = None, new_duration: int = None, new_testsQty: int = None,
                   headers: dict = None):
    update = Programs().update_program(program_id=program_id, new_program_name=new_program_name,
                                       new_duration=new_duration, new_testsQty=new_testsQty, headers=headers)
    CommonCheckers().check_status_code_200(response=update)
    return update


# get all weeks of defined program
def get_all_weeks_of_program(program_id: int, headers: dict = None):
    weeks = Programs().get_all_tasks_of_program(program_id=program_id)
    CommonCheckers().check_status_code_200(response=weeks)
    return weeks


# get all tasks of defined program
def get_all_tasks_of_program(program_id: int):
    tasks = Programs().get_all_weeks_of_program(program_id=program_id)
    CommonCheckers().check_status_code_200(response=tasks)
    return tasks


# view a specific week of a specific internship program
def get_week_by_program_id_and_number(program_id: int, week_number: int):
    week = Programs().get_week_by_program_id_and_number(program_id=program_id, week_number=week_number)
    CommonCheckers().check_status_code_200(response=week)
    return week


# create new week for specific program id
def create_new_week(week_number: int, program_id: int):
    add_week = Weeks().add_week(week_number=week_number, program_id=program_id)
    CommonCheckers().check_status_code_201(response=add_week)
    return add_week
