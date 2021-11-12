import random
from framework.utils.string import get_random_string


def create_random_user():
    user = {
        "username": get_random_string(),
        "password": get_random_string(password=True),
        "role": random.choice(["mentor", "laborant"])  # TODO Add new roles
    }
    return user
