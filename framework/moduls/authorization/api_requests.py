import requests

from framework.ustils.string import get_random_string
from config import base_url


def create_user(user_data: dict = None):
    """
    :param user_data: extra user data
    :return: requests.Response
    """

    data = {
        "username": get_random_string(),
        "password": get_random_string(password=True)
    }
    if user_data:
        data.update(user_data)

    response = requests.post(url=f"{base_url}/api/v1/user/register", json=data)
    return response


def authorisation(user_data: dict):
    """
    :param user_data: dict of username and password
    :return: requests.Response
    """

    response = requests.post(url=f"{base_url}/api/v1/auth", json=user_data)
    return response


def get_user_by_username(username: str, access_token: str = None):
    """
    :param username: username user value
    :param access_token: auth token
    :return: requests.Response
    """

    headers = {"Authorization": access_token}
    response = requests.get(url=f"{base_url}/api/v1/test/hello/{username}", headers=headers)
    return response
