import allure
import pytest
from framework.check import check_not_found, \
    check_get_one_post_userid_response, check_bad_request
from framework.jsonplaceholder_client import Client


@allure.suite('GET /post?userId=')
class TestGetOnePostUserId:

    @pytest.mark.parametrize('id', [1, 9], ids=['userId = 1', 'userId = 9'])
    def test_get_one_post_userid(self, id):
        response = Client().get_post_by_userid(id)
        check_get_one_post_userid_response(response)

    @allure.title('Negative. Get one post by userId=111. Not found')
    def test_get_one_post_userid_negativ_not_found(self):
        response = Client().get_post_by_userid(111)
        check_not_found(response)

    @pytest.mark.parametrize('id', [-1, "userId", 12345678901234567890, ""],
                             ids=['userId = -1', 'userId = userId',
                                  'userId = 12345678901234567890',
                                  'userId = None'])
    def test_get_one_post_userid_negativ_bad_request(self, id):
        response = Client().get_post_by_userid(id)
        check_bad_request(response)
