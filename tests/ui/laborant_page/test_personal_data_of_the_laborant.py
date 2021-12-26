import time

import allure
from app.ui.modules.laborant.laborant_page import LaborantOffice


def test_checking_for_the_presence_of_elements_on_the_page(open_browser_chrome, logger):
    lab_page = LaborantOffice(open_browser_chrome, LaborantOffice.authorization_url)
    lab_page.open()
    time.sleep(1)
    with allure.step("We log in on behalf of the laboratory assistant"):
        lab_page.login_to_the_page()
        time.sleep(1)
    with allure.step("we check the presence of the laborant avatar on his page"):
        lab_page.checking_the_avatar()
        time.sleep(1)
    with allure.step("Checking the correctness of the laborant name"):
        lab_page.check_name_laborant()
        time.sleep(1)
    with allure.step("We check the presence of the direction of the laboratory assistant"):
        lab_page.check_departament()
        time.sleep(1)
    with allure.step("Checking the level of English"):
        lab_page.check_language_level()
        time.sleep(1)
    with allure.step("Checking the date of birth format"):
        lab_page.check_date_of_birth_format()
        time.sleep(1)
    with allure.step("We check whether the specified phone number is digits"):
        lab_page.check_telephone_format()
        time.sleep(1)
