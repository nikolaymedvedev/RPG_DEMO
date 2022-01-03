from framework.api.api_requests import get, post, put, delete
from configs.config import get_data


class Weeks:

    def __init__(self):
        self.base_url = get_data(file_name="app_config.json")["base_url_weeks"]

    def add_week(self, week_number: int, program_id: int, headers: dict = None):
        """
        :param week_number: week number
        :param program_id: id program
        :param headers: headers request
        :return: requests.Response
        """
        data = {
            "weekNumber": week_number,
            "programID": program_id
        }
        response = post(url=f"{self.base_url}{self.week_url}", json=data, headers=headers)
        return response

    def get_week_by_id(self, week_id: int):
        """
        :param week_id: the id of the direction
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{week_id}")
        return response

    def update_week(self, week_number: int, program_id: int):
        """
        :param week_number: number of the week
        :param program_id: the id of the program
        :return: requests.Response
        """
        data = {
            "weekNumber": week_number,
            "programID": program_id
        }
        response = put(url=f"{self.base_url}{program_id}", json=data)
        return response

    def delete_week_by_id(self, week_id: int, headers: dict = None):
        """
        :param week_id: the id of the week
        :param headers: headers request
        :return: requests.Response
        """
        response = delete(url=f"{self.base_url}{week_id}", headers=headers)
        return response

    def get_all_tasks_of_week(self, week_id):
        """
        :param week_id: of the week
        :return: all tasks of week
        """
        response = get(url=f"{self.base_url}{id}/tasks")
        return response

    def get_all_literature_of_week(self, week_id: int):
        """
        :param week_id: id of the week 
        :return: all literature of week
        """
        response = get(url=f"{self.base_url}week/{week_id}/literature")
        return response

