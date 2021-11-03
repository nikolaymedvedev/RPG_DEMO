import allure
import pytest
from framework_for_example.check import check_created_response,\
    check_bad_request, check_not_found
from framework_for_example.jsonplaceholder_client import Client


@allure.suite('Post /post')
class TestAddOnePost:

    @pytest.mark.parametrize(
        'id, title, body',
        [(105, None, None), (None, "title", None), (None, None, "body"),
         (None,
          "01234567890123456789012345678901234567890123456789"
          "01234567890123456789012345678901234567890123456789"
          "01234567890123456789012345678901234567890123456789"
          "01234567890123456789012345678901234567890123456789"
          "01234567890123456789012345678901234567890123456789"
          "01234567890123456789012345678901234567890123456789",
          None),
         (None, None, "!@#$%^&*(),./ ;:-=+*&^%$#@"),
         (None, None, "DdЪъ")
         ],
        ids=['userId positiv', 'title positiv','body positiv',
             "title more then 255 symbols", "body special symbols",
             "body capital letters + language"])
    def test_add_one_post(self, id, title, body, gen2):
        response = Client().add_post(gen2(id=id, title=title, body=body))
        check_created_response(response)

    @pytest.mark.parametrize(
        'id, title, body',
        [(-1, None, None)],
        ids=['userId negativ'])
    def test_add_one_post_negativ_bad_request(self, id, title, body, gen2):
        response = Client().add_post(gen2(id=id, title=title, body=body))
        check_bad_request(response)

    @pytest.mark.parametrize(
        'id, title, body',
        [(111, None, None)],
        ids=['userId not_found'])
    def test_add_one_post_negativ_not_found(self, id, title, body, gen2):
        response = Client().add_post(gen2(id=id, title=title, body=body))
        check_not_found(response)
