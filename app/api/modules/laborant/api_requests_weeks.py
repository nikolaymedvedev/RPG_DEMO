from framework.api.api_requests import get, post, put, delete
from configs.config import get_data


class Weeks:

    def __init__(self):
        self.base_url = get_data(file_name="app_config.json")["base_url_weeks"]
        self.week_url = "/api/v1/directions/weeks/"

    def get_all_weeks(self, skip: int = 1, limit: int = 100):
        """
        :param skip: how many weeks to skip from the beginning
        :param limit: how many weeks to show
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.week_url}?skip={skip}&limit={limit}")
        return response

    def add_week(self, week_number: int, program_id: int):
        """
        :param week_number: week number
        :param program_id: id program
        :return: requests.Response
        """
        data = {
            "weekNumber": f"{week_number}",
            "programID": f"{program_id}"
        }
        response = post(url=f"{self.base_url}{self.week_url}", json=data)
        return response

    def get_week_by_id(self, week_id: int):
        """
        :param week_id: the id of the direction
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.week_url}{week_id}")
        return response

    def update_week(self, week_id: int, direction_id: int):
        """
        :param direction_id: the id of the direction
        :param week_id: the id of the week
        :return: requests.Response
        """
        data = {
            "direction_id": direction_id
        }
        response = put(url=f"{self.base_url}{self.week_url}{week_id}", json=data)
        return response

    def delete_week_by_id(self, week_id: int, headers: dict = None):
        """
        :param week_id: the id of the week
        :param headers: headers request
        :return: requests.Response
        """
        response = delete(url=f"{self.base_url}{week_id}", headers=headers)
        return response
