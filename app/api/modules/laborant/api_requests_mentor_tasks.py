from framework.api.api_requests import get, post, put, delete
from configs.config import get_data
from framework.utils.strings import get_random_string


class MentorTasks:

    def __init__(self):
        self.base_url = get_data(file_name="app_config.json")["base_url_laborant"]
        self.mentor_tasks_url = "/api/v1/directions/weeks/mentor_tasks"

    def get_all_mentor_tasks(self, skip: int = 1, limit: int = 100):
        """
        :param skip: how many mentor tasks to skip from the beginning
        :param limit:  how many mentor tasks  to show
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.mentor_tasks_url}?skip={skip}&limit={limit}")
        return response

    def create_mentor_task(self, week_id: int, description: str = get_random_string()):
        """
        :param week_id: the week id to create mentor task
        :param description: new mentor task description
        :return: requests.Response
        """
        data = {
            "description": description,
            "week_id": week_id
        }

        response = post(url=f"{self.base_url}{self.mentor_tasks_url}", json=data)
        return response

    def get_mentor_task_by_id(self, mentor_task_id: int):
        """
        :param mentor_task_id: id of the mentor task
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.mentor_tasks_url}{mentor_task_id}")
        return response

    def update_mentor_task(self, mentor_task_id: int, description: str = get_random_string()):
        """
        :param description: description to update the mentor task
        :param mentor_task_id: the id of the mentor task
        :return: requests.Response
        """
        data = {
            "description": description
        }
        response = put(url=f"{self.base_url}{self.mentor_tasks_url}{mentor_task_id}", json=data)
        return response

    def delete_mentor_task(self, mentor_task_id: int):
        """
        :param mentor_task_id: the id of the mentor task
        :return: requests.Response
        """
        response = delete(url=f"{self.base_url}{self.mentor_tasks_url}{mentor_task_id}")
        return response
