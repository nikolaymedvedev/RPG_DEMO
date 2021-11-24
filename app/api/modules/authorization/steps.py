from app.api.modules.authorization.api_requests import Authorisation
from framework.utils.checks import CommonCheckers


def create_new_user(new_user_data: dict):
    check_status_code = CommonCheckers()
    auth = Authorisation()
    create_user_response = auth.create_user(user_data=new_user_data)
    check_status_code.check_status_code_201(response=create_user_response)
    return create_user_response


def create_not_unique_new_user(user_data):
    check_status_code = CommonCheckers()
    auth = Authorisation()
    create_same_user_response = auth.create_user(user_data=user_data)
    check_status_code.check_status_code_400(response=create_same_user_response)
    return create_same_user_response


def get_user(username: str, auth_token: str):
    check_status_code = CommonCheckers()
    auth = Authorisation()
    get_user_response = auth.get_user_by_username(username=username, access_token=auth_token)
    check_status_code.check_status_code_200(response=get_user_response)
    return get_user_response


def get_user_without_auth_token(username: str):
    check_status_code = CommonCheckers()
    auth = Authorisation()
    get_user_response = auth.get_user_by_username(username=username)
    check_status_code.check_status_code_401(response=get_user_response)
    return get_user_response


def get_auth_token(user_data: dict):
    check_status_code = CommonCheckers()
    auth = Authorisation()
    get_auth_token_response = auth.authorisation(user_data=user_data)
    check_status_code.check_status_code_200(response=get_auth_token_response)
    return get_auth_token_response
