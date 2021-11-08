from framework.ustils.helpers import get_user_body
from framework.moduls.authorization.steps import create_new_user, create_new_user_with_not_unique
from tests.test_data import username_already_exists


def test_create_user_with_not_unique_values():
    # Create user
    new_user_data = get_user_body()
    create_new_user(new_user_data)

    # Create not unique user
    create_same_user_response = create_new_user_with_not_unique(new_user_data)
    assert create_same_user_response.json()["error"] == "username already exists", username_already_exists
