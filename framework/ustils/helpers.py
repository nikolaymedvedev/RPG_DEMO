from framework.ustils.string import get_random_string


def get_user_body(username: str = None, password: str = None):
    user_body = {
        "username": get_random_string(),
        "password": get_random_string(password=True)
    }
    if username:
        user_body["username"] = username
    if password:
        user_body["password"] = password
    return user_body
