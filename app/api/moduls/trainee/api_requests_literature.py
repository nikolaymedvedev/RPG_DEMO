from framework.api.api_requests import get, post, put, delete
from configs.config import get_data


class Literature:

    def __init__(self):
        self.base_url = get_data(file_name="app_config.json")["base_url_trainee"]
        self.literature_url = "/api/v1/directions/weeks/literature"

    def get_all_literature(self, skip: int = 1, limit: int = 100):
        """
        :param skip: how many literature to skip from the beginning
        :param limit: how many literature to show
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.literature_url}?skip={skip}&limit={limit}")
        return response

    def add_literature(self, literature_title: str):
        """
        :param literature_title: the title of the new literature
        :return: requests.Response
        """
        data = {
            "title": literature_title,
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

    def update_topic(self, literature_id: int, new_literature_title: str):
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

    def delete_topic(self, literature_id: int):
        """
        :param literature_id: id of the literature
        :return: requests.Response
        """
        response = delete(url=f"{self.base_url}{self.literature_url}{literature_id}")
        return response
