from app.api.modules.authorization.api_requests import Authorisation
from app.api.modules.laborant.api_requests_directions import Directions
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
