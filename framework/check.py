import allure
import json
from hamcrest import assert_that, equal_to
from requests import codes


def attach(*args):  # добавляет в allure отчет json ответа
    def _method(*args):
        response = args[0]
        allure.attach(json.dumps(response.json(), indent=4),
                      'response_body', allure.attachment_type.JSON)
    return _method


@attach
def _response_general_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}.'
                f' Actual code: {response.status_code}. Url: {response.url}')


def _response_error_check(response, expected_code=codes.not_found):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}.'
                f' Actual code: {response.status_code}. Url: {response.url}')


@allure.step('Проверка ответа GET	/posts')
def check_get_all_posts_response(response):
    _response_general_check(response)
    print(response.json())
    assert_that(len(response.json()), equal_to(100))


@allure.step('Проверка ответа GET	/post')
def check_get_one_post_response(response):
    _response_general_check(response)
    print(response.json())
    assert_that(len(response.json()), equal_to(4))


@allure.step('Проверка ответа в случае, если возвращает not_found')
def check_not_found(response):
    _response_error_check(response, codes.not_found)


@allure.step('Проверка ответа в случае, если возвращает bad_request')
def check_bad_request(response):
    _response_error_check(response, codes.bad_request)


@allure.step('Проверка ответа POST	/post')
def check_created_response(response):
    _response_general_check(response, codes.created)
    print(response.json())
    assert_that(len(response.json()), equal_to(4))


@allure.step('Проверка ответа GET	/posts?userId=')
def check_get_one_post_userid_response(response):
    _response_general_check(response)
    print(response.json())
    assert_that(len(response.json()), equal_to(10))


@allure.step('Проверка ответа GET	/posts/[id]/comments')
def check_get_comments(response):
    _response_general_check(response)
    res = response.json()
    print(res)
    keys = ['postId', 'id', 'name', 'email', 'body']
    assert_that(len(res), equal_to(5))
    for t in res:
        for k in keys:
            assert t[k]
