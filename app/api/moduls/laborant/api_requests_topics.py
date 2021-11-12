from framework.api.api_requests import get, post, put, delete
from configs.config import get_data
from app.api.helpers.laborants import get_random_direction


class Topics:

    def __init__(self):
        self.base_url = get_data(file_name="app_config.json")["base_url_laborant"]
        self.topic_url = "/api/v1/directions/weeks/topics"

    def get_all_topics(self, skip: int = 1, limit: int = 100):
        """
        :param skip: how many topics to skip from the beginning
        :param limit: how many topics to show
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.topic_url}?skip={skip}&limit={limit}")
        return response

    def create_topic(self, week_id: int, topic_title: str = get_random_direction()):
        """
        :param topic_title: the id of the topic
        :param week_id: the id of the week
        :return: requests.Response
        """
        data = {
            "title": topic_title,
            "week_id": week_id
        }
        response = post(url=f"{self.base_url}{self.topic_url}", json=data)
        return response

    def get_topic_by_id(self, topic_id: int):
        """
        :param topic_id: the id of the topic
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{self.topic_url}{topic_id}")
        return response

    def update_topic(self, topic_id: int, topic_title: str = get_random_direction()):
        """
        :param topic_title: new title for the topic
        :param topic_id: the id of the topic
        :return: requests.Response
        """
        data = {
            "title": topic_title
        }
        response = put(url=f"{self.base_url}{self.topic_url}{topic_id}", json=data)
        return response

    def delete_topic(self, topic_id: int):
        """
        :param topic_id: the id of the topic
        :return: requests.Response
        """
        response = delete(url=f"{self.base_url}{self.topic_url}{topic_id}")
        return response
