from framework.ustils.check import CommonCheckers
from framework.ustils.helpers import get_user_body
from framework.moduls.authorization.api_requests import create_user, get_user_by_username


def create_new_user(new_user_data: dict = None):
    check_status_code = CommonCheckers()
    if not new_user_data:
        new_user_data = get_user_body()
    create_user_response = create_user(user_data=new_user_data)
    check_status_code.check_status_code_201(response=create_user_response)
    return create_user_response


def create_new_user_with_not_unique(not_unique_user_data):
    check_status_code = CommonCheckers()
    create_same_user_response = create_user(user_data=not_unique_user_data)
    check_status_code.check_status_code_400(response=create_same_user_response)
    return create_same_user_response


def get_user(username, auth_token):
    check_status_code = CommonCheckers()
    get_user_response = get_user_by_username(username=username, access_token=auth_token)
    check_status_code.check_status_code_200(response=get_user_response)
    return get_user_response
