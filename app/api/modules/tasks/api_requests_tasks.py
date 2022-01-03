from app.api.helpers.laborants import get_random_number, get_title, get_description, get_deadline_date,\
    get_random_priority, get_random_status
from framework.api.api_requests import get, post, put, delete
from configs.config import get_data


class Tasks:

    def __init__(self):
        self.base_url = get_data(file_name="browser_config.json")["base_url_tasks"]

    def get_task_by_id(self, task_id: int, headers: dict = None):
        """
        :param headers: headers request
        :param task_id: id task
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{task_id}", headers=headers)
        return response

    def create_task(self, weekID: int, title: str = None, description: str = None,
                    deadline: str = None, timeSpent: int = None, priority: str = None,
                    status: str = None, headers: dict = None):
        """
        :param title: title task
        :param description: description task
        :param weekID : id week for task
        :param deadline: end date
        :param timeSpent: how much time was spent on the task
        :param priority: task priority
        :param status: task status
        :param headers: request headers
        """
        new_title = get_title()
        if title:
            new_title = title
        new_description = get_description()
        if description:
            new_description = description
        new_deadline = get_deadline_date()
        if deadline:
            new_deadline = deadline
        new_time_spent = get_random_number()
        if timeSpent:
            new_time_spent = timeSpent
        new_priority = get_random_priority()
        if priority:
            new_priority = priority
        new_status = get_random_status()
        if status:
            new_status = status
        data = {
                "title": f"{new_title}",
                "description": f"{new_description}",
                "weekID": f"{weekID}",
                "deadline": f"{new_deadline}",
                "timeSpent": f"{new_time_spent}",
                "priority": f"{new_priority}",
                "status": f"{new_status}"
            }
        response = post(url=f"{self.base_url}",
                        json=data,
                        headers=headers)
        return response

    def update_task(self, task_id: int, weekID: int, title: str = None, description: str = None,
                    deadline: str = None, timeSpent: int = None, priority: str = None,
                    status: str = None, headers: dict = None):
        """
        :param task_id: id of the task
        :param title: title task
        :param description: descriotion task
        :param weekID : id week for task
        :param deadline: end date
        :param timeSpent: how much time was spent on the task
        :param priority: task priority
        :param status: task status
        :param headers: request headers
        """
        new_title = get_title()
        if title:
            new_title = title
        new_description = get_description()
        if description:
            new_description = description
        new_deadline = get_deadline_date()
        if deadline:
            new_deadline = deadline
        new_time_spent = get_random_number()
        if timeSpent:
            new_time_spent = timeSpent
        new_priority = get_random_priority()
        if priority:
            new_priority = priority
        new_status = get_random_status()
        if status:
            new_status = status
        data = {
            "title": f"{new_title}",
            "description": f"{new_description}",
            "weekID": f"{weekID}",
            "deadline": f"{new_deadline}",
            "timeSpent": f"{new_time_spent}",
            "priority": f"{new_priority}",
            "status": f"{new_status}"
        }
        response = put(url=f"{self.base_url}{task_id}",
                       json=data,
                       headers=headers)
        return response

    def delete_task_by_id(self, task_id: int, headers: dict = None):
        """
        :param task_id: id of the task
        :param headers: request headers
        :return: requests.Response
        """
        response = delete(url=f"{self.base_url}{task_id}", headers=headers)
        return response
