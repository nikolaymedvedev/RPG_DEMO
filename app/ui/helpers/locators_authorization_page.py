from selenium.webdriver.common.by import By


class AuthorizationPageLocators:

    LOCATOR_AUTHORIZATION_PAGE_MAIN_MESSAGE = (By.XPATH, "//h2['Вход в систему']")

    LOCATOR_LOGIN_FIELD = (By.XPATH, "//input[@type='text' and @name='login']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOCATOR_UNCOVER_PASSWORD = (By.XPATH, "//input[@type='password']/../span")
    LOCATOR_ENTER_BUTTON = (By.XPATH, "//button[@type='submit']")

    LOCATOR_ALERT_NOT_VALID_LOGIN_OR_PASSWORD = (By.XPATH, "//div/span[2][text()='Неверные логин или пароль.']")
    LOCATOR_ALERT_REQUIRED_FIELD_LOGIN = (By.XPATH, "//div/span[1][text()='Обязательное поле']")
    LOCATOR_ALERT_REQUIRED_FIELD_PASSWORD = (By.XPATH, "//div/span[2][text()='Обязательное поле']")
    LOCATOR_ALERT_PASSWORD_LENGTH = (By.XPATH, "//div/span[2][text()='Пароль должен содержать 12 символов']")

    LOCATOR_INPUT_FIELDS = (By.TAG_NAME, "input")
    LOCATOR_BUTTON_LINK = (By.XPATH, "//div/div[2]/form/span")
    LOCATOR_BUTTON_LINK_HEADING = (By.XPATH, "//form/div[3]/div/h2")
    LOCATOR_BUTTON_LINK_FIELD = (By.XPATH, "//form/div[3]/div/p")
    LOCATOR_CHECK_BUTTON = (By.TAG_NAME, "button")

class laboratoryAssistantOfficePageLocators:

    """
    :: Локаторы личной информации
    """
    LOCATOR_ALL_PERSONAL_DATA = (By.TAG_NAME, ".LaborantProfileelements__LaborantLabel-sc-shj2ft-5")
    LOCATOR_ASSISTANT_NAME = (By.CLASS_NAME, "LaborantProfileelements__LaborantHeader-sc-shj2ft-1")
    LOCATOR_ASSISTANT_BIRTHDAY = (By.XPATH, "//label[text()='Дата рождения']")
    LOCATOR_ASSISTANT_DIRECTION = (By.XPATH, "//label[text()='Направление']")
    LOCATOR_ASSISTANT_EMAIL = (By.XPATH, "//label[text()='E-mail']")
    LOCATOR_ASSISTANT_MENTOR = (By.XPATH, "//label[text()='Ментор']")
    LOCATOR_ASSISTANT_LANGUAGE = (By.XPATH, "//div/div[2]/div[5]/div/label")
    LOCATOR_ASSISTANT_LOCATION = (By.XPATH, "//label[text()='Локация']")
    LOCATOR_ASSISTANT_TELEPHONE = (By.XPATH, "//label[text()='Телефон']")
    LOCATOR_ASSISTANT_SKYPE = (By.XPATH, "//label[text()='Skype']")
    LOCATOR_ASSISTANT_AWARDS = (By.XPATH, "//label[text()='Награды']")

    """
    :: Локаторы переключаемых элементов
    """
    LOCATOR_ASSISTANT_ALL_SWITCHABLE_LEMENTS = (By.CSS_SELECTOR, ".Switcherelements__SwitcherButton-sc-as4453-1")
    LOCATOR_ASSISTANT_TIMELINE = (By.XPATH, "//div[2]/div[2]/div[2]/div[1]")
    LOCATOR_ASSISTANT_PROJECT = (By.XPATH, "//div[2]/div[2]/div[2]/div[2]")
    LOCATOR_ASSISTANT_TIMESHEETS = (By.XPATH, "//div[2]/div[2]/div[2]/div[3]")
    LOCATOR_ASSISTANT_TASKS = (By.XPATH, "//div[2]/div[2]/div[2]/div[4]")

    """
    :: Локаторы таблицы переключаемых элементов
    """
    LOCATOR_ASSISTANT_PROJECT_PROJECT = (By.XPATH, "//div/table/tbody/tr[1]/td[1]")
    LOCATOR_ASSISTANT_PROJECT_START_DATE = (By.XPATH, "//div/table/tbody/tr[1]/td[2]")
    LOCATOR_ASSISTANT_PROJECT_NUMBER_OF_PARTICIPANS = (By.XPATH, "//div/table/tbody/tr[1]/td[3]")
    LOCATOR_ASSISTANT_PROJECT_PM_PROJECT = (By.XPATH, "//div/table/tbody/tr[1]/td[4]")

    """
    :: Локаторы для элементов скрытой панели
    """
    LOCATOR_ASSISTANT_LOGO_ANDERSEN = (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/img")
    LOCATOR_ASSISTANT_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//div[1]/ul/li[1]/a/img")
    LOCATOR_ASSISTANT_LIST_OF_PARTICIPANS = (By.XPATH, "//div[1]/ul/li[2]/a/img")
    LOCATOR_ASSISTANT_HIDDEN_MENU_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/img")
    LOCATOR_ASSISTANT_NOTIFICATIONS = (By.XPATH, "//div/div[1]/div[3]/a/img")
    LOCATOR_ASSISTANT_EXIT_BUTTON = (By.XPATH, "//div/div[1]/div[3]/div[1]/img")
    LOCATOR_ASSISTANT_HIDDEN_EXIT_BUTTON = (By.XPATH, "//div[3]/div[2]/div")
    LOCATOR_EXIT_CONFIRMATION_BUTTON = (By.XPATH, "//../div[2]/button[2]")
    LOCATOR_EXIT_DENIAL_BUTTON = (By.XPATH, "//../div[2]/button[1]")
    LOCATOR_EXIT_WARNING = (By.XPATH, "//div[1]/div[3]/div[3]/div/div[1]/p")
