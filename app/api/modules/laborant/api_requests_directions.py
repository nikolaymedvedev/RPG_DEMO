from framework.api.api_requests import get, post, put, delete
from configs.config import get_data
from app.api.helpers.laborants import get_random_direction, get_random_direction_name

class Directions:

    def __init__(self):
        self.base_url = get_data(file_name="app_config.json")["base_url_authorization"]
        self.directions_url = "/api/v1/directions/"
        self.directions_url_delete_by_id = "/api/v1/directions/by_ids/"
        self.directions_url_delete_by_name = "/api/v1/directions/by_names/"
        self.directions_url_update = "/api/v1/directions/update/"

    def get_all_directions(self, skip: int = 1, limit: int = 100):
        """
        :param skip: how many directions to skip from the beginning
        :param limit: how many directions to show
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.directions_url}?skip={skip}&limit={limit}")
        return response

    def add_direction(self, direction_name: str = None, headers: dict = None):
        """
        :param direction_name: the name of the new direction
        :param headers: request headers
        :return: requests.Response
        """
        data = get_random_direction_name()
        if direction_name:
            data = direction_name
        response = post(url=f"{self.base_url}{self.directions_url}", files={"name": (None, data)},
                        headers=headers)
        return response

    def update_direction(self, direction_id: int, new_direction_name: str = None,
                         headers: dict = None):
        """
        :param direction_id: the id of the new direction
        :param new_direction_name: new direction name
        :param headers: request headers
        :return: requests.Response
        """
        new_data = get_random_direction_name()
        if new_direction_name:
            new_data = new_direction_name
        response = post(url=f"{self.base_url}{self.directions_url_update}{direction_id}", files={"name": (None, new_data)},
                        headers=headers)
        return response

    def get_direction_by_id(self, direction_id: int):
        """
        :param direction_id: the id of the direction
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.directions_url}{direction_id}")
        return response

    def delete_direction_by_id(self, direction_id: int, headers: dict = None):
        """
        :param direction_id: id of the direction
        :param headers: request headers
        :return: requests.Response
        """
        response = delete(url=f"{self.base_url}{self.directions_url_delete_by_id}{direction_id}/",
                          headers=headers)
        return response

    def delete_direction_by_name(self, direction_name: str, headers: dict = None):
        """
        :param direction_name: name of the direction
        :param headers: request headers
        :return: requests.Response
        """
        response = delete(url=f"{self.base_url}{self.directions_url_delete_by_name}{direction_name}/",
                          headers=headers)
        return response
