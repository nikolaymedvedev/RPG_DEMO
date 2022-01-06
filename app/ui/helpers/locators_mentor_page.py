from selenium.webdriver.common.by import By


class MentorPageLocators:

    LOCATOR_MENTOR_NAME = (By.TAG_NAME, "h1")
    LOCATOR_MENTOR_PHOTO = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/img")
    LOCATOR_MENTOR_LOCATION = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/p[2]")
    LOCATOR_MENTOR_PHONE_NUMBER = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div[3]/p[2]")
    LOCATOR_MENTOR_EMAIL = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div[4]/a")
    LOCATOR_MENTOR_SKYPE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div[5]/a")

    LOCATOR_LABORANTS = (By.XPATH, "//div[text()='Мои лаборанты']")
    LOCATOR_TASK_LIST = (By.XPATH, "//div[text()='Список задач']")
    LOCATOR_ARCHIVE = (By.XPATH, "//div[text()='Архив']")

    LOCATOR_BUTTON_PERSONAL_ROOM = (By.XPATH, "/html/body/div[1]/div/div[1]/ul/li[1]/a/img")
    LOCATOR_BUTTON_SEARCH = (By.XPATH, "/html/body/div[1]/div/div[1]/ul/li[2]/a/img")
    LOCATOR_BUTTON_NOTIFICATIONS = (By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/a/img")
    LOCATOR_BUTTON_MY_PROFILE = (By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[1]/img")
    LOCATOR_BUTTON_QUIT = (By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[2]/div")
    LOCATOR_BUTTON_QUIT_YES = (By.XPATH, "//button[text()='Да']")
    LOCATOR_BUTTON_QUIT_NO = (By.XPATH, "//button[text()='Нет']")


    LOCATOR_FIRST_LABORANT_MENU = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td["
                                             "7]/div/div[1]")
    LOCATOR_FIRST_LABORANT_MENU_COMPLETE_THE_LAB = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div["
                                                              "2]/table/tbody/tr[1]/td[7]/div/div[2]/div/div[1]")
    LOCATOR_FIRST_LABORANT_MENU_COMPLETE_ASSIGN_AN_EXAM = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div["
                                                                     "2]/table/tbody/tr[1]/td[7]/div/div[2]/div/div["
                                                                     "2]")

    LOCATOR_FIRST_LABORANT = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]")
    LOCATOR_FIRST_LABORANT_TIMELINE = (By.XPATH, "//div[contains(text(),'Timeline')]")
    LOCATOR_FIRST_LABORANT_PROJECT = (By.XPATH, "//div[contains(text(),'Проект')]")
    LOCATOR_FIRST_LABORANT_PROJECT_ONE_TEAM = (By.XPATH, "//div//tr[2]/td[3]/p")
    LOCATOR_FIRST_LABORANT_PROJECT_ONE_TEAM_CLOSE = (By.CSS_SELECTOR,
                                                     ".ProjectModalelements__ModalTableIcon-sc-ovr6np-7.hKdPOM")
    LOCATOR_FIRST_LABORANT_TIMESHEETS = (By.XPATH, "//div[contains(text(),'Timesheets')]")
    LOCATOR_FIRST_LABORANT_TASKS = (By.XPATH, "//div[contains(text(),'Задачи')]")
    LOCATOR_FIRST_LABORANT_INFO = (By.XPATH, "//div[contains(text(),'О лаборанте')]")
    LOCATOR_FIRST_LABORANT_INFO_FEEDBACK = (By.XPATH, "//button[text()='Добавить фидбэк']")
    LOCATOR_FIRST_LABORANT_INFO_FEEDBACK_TEXTAREA = (By.ID, "feedback")
    LOCATOR_FIRST_LABORANT_INFO_FEEDBACK_CANCEL = (By.XPATH, "//button[text()='Отмена']")
    LOCATOR_FIRST_LABORANT_INFO_FEEDBACK_ADD = (By.XPATH, "//button[text()='Добавить']")
    LOCATOR_FIRST_LABORANT_INFO_ADD_CV = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[3]/section/div[2]/div["
                                                    "2]/div[1]/button")
    LOCATOR_FIRST_LABORANT_INFO_ADD_TECH_SPEC = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[3]/section/div["
                                                           "2]/div[2]/div[2]/button")
