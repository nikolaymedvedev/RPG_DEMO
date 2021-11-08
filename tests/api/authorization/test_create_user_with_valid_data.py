from framework.moduls.authorization.api_requests import authorisation
from framework.moduls.authorization.steps import create_new_user, get_user
from framework.ustils.helpers import get_user_body
from tests.test_data import username_already_exists


def test_create_user_with_valid_data():
    # Create user
    new_user_data = get_user_body()
    create_user_response = create_new_user(new_user_data)

    # Get auth token
    create_user_response.json()
    auth_token = authorisation(user_data=new_user_data).json()["jwt"]

    # Check if new user is present
    get_user_response = get_user(username=new_user_data["username"], auth_token=auth_token)
    assert get_user_response.json()["hello_response"] == f"Hello {new_user_data['username']}!", username_already_exists
