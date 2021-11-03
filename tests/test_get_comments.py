import allure
from framework.check import check_get_comments
from framework.jsonplaceholder_client import Client


@allure.suite('GET /posts//comments')
class TestGetComments:

    @allure.title('Positive. Get comments')
    def test_get_comments(self):
        response = Client().get_comments(2)
        check_get_comments(response)
