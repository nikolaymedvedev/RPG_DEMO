import pytest
from framework_for_example.logging import Logging
from framework_for_example.helper import gen


@pytest.fixture(scope='session', autouse=True)
def logger():  # включает логирование
    log = Logging()
    logger = log.logging()
    yield logger


@pytest.fixture(scope='session')
def gen1():
    yield gen()


@pytest.fixture(scope='function')
def gen2(gen1):
    """
    генерирует json с рандомными значениями
    и если нужно подставляет в него переданные аргументы
    :param gen1:
    :return:
    """
    def _method(id=None, title=None, body=None):
        data = next(gen1)
        if id:
            data["userId"] = id
        if title:
            data["title"] = title
        if body:
            data["body"] = body
        return data

    return _method
