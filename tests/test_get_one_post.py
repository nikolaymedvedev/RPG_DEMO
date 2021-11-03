import allure
import pytest
from framework.check import check_get_one_post_response, check_not_found, \
    check_bad_request
from framework.jsonplaceholder_client import Client


@allure.suite('GET /post')
class TestGetOnePost:

    @pytest.mark.parametrize('id', [1, 5, 100],
                             ids=['id = 1', 'id = 5', 'id = 100'])
    def test_get_one_post(self, id):
        response = Client().get_post_by_id(id)
        check_get_one_post_response(response)

    @pytest.mark.parametrize('id', [0, -1, 101],
                             ids=['id = 0', 'id = -1', 'id=101'])
    def test_get_one_post_negativ_not_found(self, id):
        response = Client().get_post_by_id(id)
        check_not_found(response)

    @pytest.mark.parametrize('id',
                             [1.2, '1,2', "userId", 1234567890123456789, ""],
                             ids=['userId = 1.2', 'userId = 1,2',
                                  'userId = userId',
                                  'userId = 1234567890123456789',
                                  'userId = None'])
    def test_get_one_post_negativ_bad_request(self, id):
        response = Client().get_post_by_id(id)
        check_bad_request(response)
