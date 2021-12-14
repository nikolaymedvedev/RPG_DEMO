from selenium.webdriver.common.by import By


class laboratoryAssistantLocators:

    """
    :: Personal Information Locators
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
    LOCATOR_ASSISTANT_PERSONAL_DATA_HEADER_OF_THE_PAGE = (By.XPATH, "//p[text()='Личный кабинет']")
    LOCATOR_ASSISTANT_PARTICIPANTS_HEADER_OF_THE_PAGE = (By.XPATH, "//p[text()='Список Участников']")

    """
    :: Locators of switchable elements
    """
    LOCATOR_ASSISTANT_ALL_SWITCHABLE_ELEMENTS = (By.CSS_SELECTOR, ".Switcherelements__SwitcherButton-sc-as4453-1")
    LOCATOR_ASSISTANT_BUTTON_TIMELINE = (By.XPATH, "//div[2]/div[2]/div[2]/div[1]")
    LOCATOR_ASSISTANT_BUTTON_PROJECT = (By.XPATH, "//div[2]/div[2]/div[2]/div[2]")
    LOCATOR_ASSISTANT_BUTTON_TIMESHEETS = (By.XPATH, "//div[2]/div[2]/div[2]/div[3]")
    LOCATOR_ASSISTANT_BUTTON_TASKS = (By.XPATH, "//div[2]/div[2]/div[2]/div[4]")
    LOCATOR_OF_THE_ELEMENTS_OF_THE_PROJECT_TOGGLE_BUTTON = (By.CSS_SELECTOR, ".ProjectTableelements__ProjectHeader-sc-iv8bmm-3.KmPXG")

    """
    :: Locators of the table of the switchable element 'project'
    """
    LOCATOR_ASSISTANT_PROJECT_PROJECT = (By.XPATH, "//div/table/tbody/tr[1]/td[1]")
    LOCATOR_ASSISTANT_PROJECT_START_DATE = (By.XPATH, "//div/table/tbody/tr[1]/td[2]")
    LOCATOR_ASSISTANT_PROJECT_NUMBER_OF_PARTICIPANS = (By.XPATH, "//div/table/tbody/tr[1]/td[3]")
    LOCATOR_ASSISTANT_PROJECT_PM_PROJECT = (By.XPATH, "//div/table/tbody/tr[1]/td[4]")

    """
    :: Locators for hidden panel elements
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