import allure
from examples.framework_for_example.check import check_get_comments
from examples.framework_for_example.jsonplaceholder_client import Client


@allure.suite('GET /posts//comments')
class TestGetComments:

    @allure.title('Positive. Get comments')
    def test_get_comments(self):
        response = Client().get_comments(2)
        check_get_comments(response)
