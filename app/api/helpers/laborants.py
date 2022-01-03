import random
import datetime


def get_random_direction_name():
    return random.choice(["AQA", "QA", "JavaScript", "Java", "Scala", "PHP", "PHP Magento",
                          ".NET", "Python", "Ruby", "GoLang", "iOS", "Android", "Business Analysis",
                          "System Analysis", "Data engineering", "Machine Learning", "UI/UX Design",
                          "Graphic Design"])


def get_random_number():
    return random.choice(range(1, 100))


def get_title():
    return "The main title for the current task"


def get_description():
    return "Some description of the current task"


def get_deadline_date():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=14)
    return str(tomorrow.strftime('%Y-%d-%m'))


def get_random_priority():
    return random.choice([
        "Blocker", "Critical", "Major", "Minor", "Medium", "Highest", "Low", "High", "Lowest"
    ])


def get_random_status():
    return random.choice(["Open", "Assign", "Dev", "Test", "Close"])
