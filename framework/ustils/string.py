import random
from string import ascii_letters


def get_random_string(email=False, password=False, website=False, linkedin=False):
    random_string = ''
    for _ in range(random.randint(6, 12)):
        random_string += random.choice(ascii_letters)
    if email:
        random_string += '@mail.com'
    if password:
        random_string = random_string[0].upper() + random_string[1].lower() \
                        + random_string[2:].replace(random_string[2], "0")
    if website:
        random_string = f"https://www.{random_string.lower()}.com"
    if linkedin:
        random_string = f"https://www.linkedin.com/in/{get_random_string().lower()}"
    return random_string
