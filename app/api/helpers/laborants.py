import random


def get_random_direction():
    return {
        "title": random.choice(["AQA", "QA", "JavaScript", "Java", "Scala", "PHP", "PHP Magento",
                                ".NET", "Python", "Ruby", "GoLang", "iOS", "Android", "Business Analysis",
                                "System Analysis", "Data engineering", "Machine Learning", "UI/UX Design",
                                "Graphic Design"])
    }


def get_random_direction_name():
    return random.choice(["AQA", "QA", "JavaScript", "Java", "Scala", "PHP", "PHP Magento",
                                ".NET", "Python", "Ruby", "GoLang", "iOS", "Android", "Business Analysis",
                                "System Analysis", "Data engineering", "Machine Learning", "UI/UX Design",
                                "Graphic Design"])
