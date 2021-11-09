from app.api.helpers.users import create_random_user
from framework.api.api_requests import get, post
from configs.config import get_data


class Authorisation:

    def __init__(self):
        self.base_url = get_data(file_name="app_config.json")["base_url"]

    def create_user(self, user_data: dict = None):
        """
        :param user_data: new user extra data
        :return: requests.Response
        """
        data = create_random_user()
        if user_data:
            data.update(user_data)
        response = post(url=f"{self.base_url}/api/v1/user/register", json=data)
        return response

    def authorisation(self, user_data: dict):
        """
        :param user_data: dict of username and password
        :return: requests.Response
        """
        response = post(url=f"{self.base_url}/api/v1/auth", json=user_data)
        return response

    def get_user_by_username(self, username: str, access_token: str = None):
        """
        :param username: username user value
        :param access_token: auth token
        :return: requests.Response
        """
        headers = {"Authorization": access_token}
        response = get(url=f"{self.base_url}/api/v1/test/hello/{username}", headers=headers)
        return response
