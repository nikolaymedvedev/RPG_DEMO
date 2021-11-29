import random
from framework.utils.strings import get_random_string


def create_random_user():
    user = {
        "username": f"{get_random_string()}@andersenlab.com",
        "password": get_random_string(password=True),
        "role": random.choice(["mentor", "laborant", "coordinator"])  # TODO Add new roles
    }
    return user
