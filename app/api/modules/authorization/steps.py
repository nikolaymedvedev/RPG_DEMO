from app.api.modules.authorization.api_requests import Authorisation
from app.api.modules.laborant.api_requests_directions import Directions
from app.api.modules.laborant.api_requests_programs import Programs
from app.api.modules.laborant.api_requests_tasks import Tasks
from app.api.modules.laborant.api_requests_weeks import Weeks
from framework.utils.checks import CommonCheckers
from configs.base_users_for_ui_and_api_tests import base_coordinator_user


def create_new_user(new_user_data: dict):
    create_user_response = Authorisation().create_user(user_data=new_user_data)
    CommonCheckers().check_status_code_201(response=create_user_response)
    return create_user_response


def create_not_unique_new_user(user_data):
    create_same_user_response = Authorisation().create_user(user_data=user_data)
    CommonCheckers().check_status_code_400(response=create_same_user_response)
    return create_same_user_response


def get_user(username: str, auth_token: str):
    get_user_response = Authorisation().get_user_by_username(username=username, access_token=auth_token)
    CommonCheckers().check_status_code_200(response=get_user_response)
    return get_user_response


def get_user_without_auth_token(username: str):
    get_user_response = Authorisation().get_user_by_username(username=username)
    CommonCheckers().check_status_code_401(response=get_user_response)
    return get_user_response


def get_auth_token(user_data: dict):
    get_auth_token_response = Authorisation().authorisation(user_data=user_data)
    CommonCheckers().check_status_code_200(response=get_auth_token_response)
    return get_auth_token_response


def authorize_not_register_user(user_data: dict):
    get_auth_response = Authorisation().authorisation(user_data=user_data)
    CommonCheckers().check_status_code_400(response=get_auth_response)
    return get_auth_response


def delete_user_by_user_id(user_id: int, access_token: str):
    delete_user_response = Authorisation().delete_user_by_user_id(user_id=user_id, access_token=access_token)
    try:
        CommonCheckers().check_status_code_200(response=delete_user_response)
    except CommonCheckers().check_status_code_403(response=delete_user_response):
        return "user is laborant, can't delete it"
    return delete_user_response


def delete_user(user_data: dict, user_id: int):
    if user_data["role"] != "laborant":
        auth_token = get_auth_token(user_data=user_data).json()["token"]
        delete_user_response = delete_user_by_user_id(user_id, auth_token)
    else:
        auth_token = get_auth_token(user_data=base_coordinator_user).json()["token"]
        delete_user_response = delete_user_by_user_id(user_id, auth_token)
    return delete_user_response.json()


# creating a new direction
def create_direction(headers: dict, direction_name: str = None, ):
    direction = Directions().add_direction(headers=headers, direction_name=direction_name)
    CommonCheckers().check_status_code_201(response=direction)
    return direction


# create invalid direction
def create_invalid_direction(headers: dict, direction_name: str = None, ):
    direction = Directions().add_direction(headers=headers, direction_name=direction_name)
    CommonCheckers().check_status_code_400(response=direction)
    return direction


# creating an existing direction
def create_existing_direction(headers: dict, direction_name: str = None, ):
    existing_direction = Directions().add_direction(headers=headers, direction_name=direction_name)
    CommonCheckers().check_status_code_400(response=existing_direction)
    return existing_direction


# delete direction by id
def delete_direction_by_id(direction_id: int, headers: dict):
    delete_direction = Directions().delete_direction_by_id(direction_id=direction_id, headers=headers)
    CommonCheckers().check_status_code_200(response=delete_direction)
    return delete_direction


# delete direction by name
def delete_direction_by_name(direction_name: str, headers: dict):
    delete_direction = Directions().delete_direction_by_name(direction_name=direction_name, headers=headers)
    CommonCheckers().check_status_code_200(response=delete_direction)
    return delete_direction


# update direction name
def update_direction(direction_id: int, new_direction_name: str = None, headers: dict = None):
    new_direction = Directions().update_direction(direction_id=direction_id,
                                                  new_direction_name=new_direction_name,
                                                  headers=headers
                                                  )
    CommonCheckers().check_status_code_200(response=new_direction)
    return new_direction


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


# delete week
def delete_week(week_id: int, headers: dict = None):
    delete = Weeks().delete_week_by_id(week_id=week_id, headers=headers)
    CommonCheckers().check_status_code_200(response=delete)
    return delete


# view the task by its id
def get_task_by_id(task_id: int, headers: dict = None):
    task = Tasks().get_task_by_id(task_id=task_id, headers=headers)
    CommonCheckers().check_status_code_200(response=task)
    return task


# creating a new task
def create_new_task(weekID: int, title: str = None, description: str = None,
                    deadline: str = None, timeSpent: int = None, priority: str = None,
                    status: str = None, headers: dict = None):
    task = Tasks().create_task(weekID=weekID, title=title, description=description,
                               deadline=deadline, timeSpent=timeSpent, priority=priority,
                               status=status, headers=headers)
    CommonCheckers().check_status_code_201(response=task)
    return task


# updating a task
def update_task(task_id: int, weekID: int, title: str = None, description: str = None,
                deadline: str = None, timeSpent: int = None, priority: str = None,
                status: str = None, headers: dict = None):
    new_task = Tasks().update_task(task_id=task_id, weekID=weekID, title=title, description=description,
                                   deadline=deadline, timeSpent=timeSpent, priority=priority,
                                   status=status, headers=headers)
    CommonCheckers().check_status_code_200(response=new_task)
    return new_task


# deleting a task by id
def delete_new_task_by_id(task_id: int, headers: dict = None):
    delete = Tasks().delete_task_by_id(task_id=task_id, headers=headers)
    CommonCheckers().check_status_code_200(response=delete)
    return delete
