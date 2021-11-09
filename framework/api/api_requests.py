import requests
from framework.logger.logger import Logger


def get(url: str, headers: dict = None):
    logger = Logger()
    try:
        response = requests.get(url=url, headers=headers)
        logger.api(response=response)
        return response
    except ConnectionError as err:
        logger.error(msg=err)


def post(url: str, data: dict = None, json: dict = None, files=None):
    logger = Logger()
    try:
        response = requests.post(url=url, data=data, json=json, files=files)
        logger.api(response=response)
        return response
    except ConnectionError as err:
        logger.error(msg=err)


def put(url: str, data: dict = None, json: dict = None):
    logger = Logger()
    try:
        response = requests.put(url=url, data=data, json=json)
        logger.api(response=response)
        return response
    except ConnectionError as err:
        logger.error(msg=err)


def delete(url: str, params: dict = None):
    logger = Logger()
    try:
        response = requests.delete(url=url, params=params)
        logger.api(response=response)
        return response
    except ConnectionError as err:
        logger.error(msg=err)
