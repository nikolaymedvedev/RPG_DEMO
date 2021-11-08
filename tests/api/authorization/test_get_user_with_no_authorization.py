from framework.moduls.authorization.api_requests import get_user_by_username
from framework.moduls.authorization.steps import create_new_user
from framework.ustils.check import CommonCheckers
from framework.ustils.helpers import get_user_body


def test_get_user_with_no_authorization():
    # Create user
    new_user_data = get_user_body()
    check_status_code = CommonCheckers()
    create_new_user(new_user_data=new_user_data)

    # Check if new user is present
    get_user_response = get_user_by_username(username=new_user_data["username"])
    check_status_code.check_status_code_401(response=get_user_response)
    assert get_user_response.json() == "Unauthorized", "Unauthorized message is not exist"
