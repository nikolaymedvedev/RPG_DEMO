from framework.api.api_requests import get, post, put, delete
from configs.config import get_data


class Directions:

    def __init__(self):
        self.base_url = get_data(file_name="app_config.json")["base_url_trainee"]
        self.directions_url = "/api/v1/directions/"

    def get_all_directions(self, skip: int = 1, limit: int = 100):
        """
        :param skip: how many directions to skip from the beginning
        :param limit: how many directions to show
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.directions_url}?skip={skip}&limit={limit}")
        return response

    def add_direction(self, direction_title: str):
        """
        :param direction_title: the title of the new direction
        :return: requests.Response
        """
        data = {
            "title": direction_title,
        }
        response = post(url=f"{self.base_url}{self.directions_url}", json=data)
        return response

    def get_direction_by_id(self, direction_id: int):
        """
        :param direction_id: the id of the direction
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.directions_url}{direction_id}")
        return response

    def update_direction(self, direction_id: int, new_direction_title: str):
        """
        :param new_direction_title: new title for the direction
        :param direction_id: id of the direction
        :return: requests.Response
        """
        data = {
            "title": new_direction_title
        }
        response = put(url=f"{self.base_url}{self.directions_url}{direction_id}", json=data)
        return response

    def delete_direction(self, direction_id: int):
        """
        :param direction_id: id of the direction
        :return: requests.Response
        """
        response = delete(url=f"{self.base_url}{self.directions_url}{direction_id}")
        return response
