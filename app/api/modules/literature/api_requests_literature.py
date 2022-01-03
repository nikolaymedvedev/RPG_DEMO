from framework.api.api_requests import get, post, put, delete
from configs.config import get_data
from framework.utils.strings import get_random_string


class Literature:

    def __init__(self):
        self.base_url = get_data(file_name="browser_config.json")["base_url_literature"]

    def get_all_literature(self, skip: int = 1, limit: int = 100):
        """
        :param skip: how many literature to skip from the beginning
        :param limit: how many literature to show
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}")
        return response

    def add_literature(self, week_id: int, literature_title: str = None):
        """
        :param week_id: id of the week
        :param literature_title: the title of the new literature
        :return: requests.Response
        """
        title = get_random_string()
        if literature_title:
            title = literature_title
        data = {
            "title": title,
            "weekID": week_id
        }
        response = post(url=f"{self.base_url}{self.literature_url}", json=data)
        return response

    def get_literature_by_id(self, literature_id: int):
        """
        :param literature_id: the id of the literature
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.literature_url}{literature_id}")
        return response

    def update_topic(self, literature_id: int, new_literature_title: get_random_string()):
        """
        :param new_literature_title: new title for the literature
        :param literature_id: id of the literature
        :return: requests.Response
        """
        data = {
            "title": new_literature_title
        }
        response = put(url=f"{self.base_url}{self.literature_url}{literature_id}", json=data)
        return response

    def delete_literature(self, literature_id: int):
        """
        :param literature_id: id of the literature
        :return: requests.Response
        """
        response = delete(url=f"{self.base_url}{literature_id}")
        return response
