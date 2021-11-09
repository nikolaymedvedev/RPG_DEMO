import allure
import requests as r
from configs.config import JSONPLACEHOLDER_HOST


class Client:

    def url(func):
        def wrapper(*args):
            response = func(*args)
            allure.dynamic.description(response.request.method + ': '
                                       + response.request.url)
            return response

        return wrapper

    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    def _post(self, data, path: str):
        headers = {'Content-Type': 'application/json'}
        return r.post(url=JSONPLACEHOLDER_HOST + path,
                      headers=headers, json=data)

    @url
    @allure.step('Отправка запроса GET	/posts')
    def get_all_posts(self):
        return self._get(path=f'/posts')

    @url
    @allure.step('Отправка запроса GET	/post/[post_id]')
    def get_post_by_id(self, post_id: int):
        return self._get(path=f'/posts/{post_id}')

    @url
    @allure.step('Отправка запроса POST	/posts')
    def add_post(self, data):
        return self._post(data, path=f'/posts')

    @url
    @allure.step('Отправка запроса GET	/posts?userId=')
    def get_post_by_userid(self, user_id: int):
        return self._get(path=f'/posts?userId={user_id}')

    @url
    @allure.step('Отправка запроса GET	/posts/[id]/comments')
    def get_comments(self, id: int):
        return self._get(path=f'/posts/{id}/comments')
