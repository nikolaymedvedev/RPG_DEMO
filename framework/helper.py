import json
import random


def gen(title=None, body=None, id=None):
    id = 300
    while True:
        title = str(random.randint(1, 100))
        body = str(random.randint(1, 100))
        id += 1
        data = json.loads(
            '''{{"userId": {id}, "title": "{title}", "body": "{body}"}}'''
            .format(id=id, title=title, body=body))
        yield data
