from selenium.webdriver.common.by import By


class LaborantPageLocators:
    """
    :: Personal Information Locators
    """
    LOCATOR_ALL_PERSONAL_DATA = (By.TAG_NAME, ".LaborantProfileelements__LaborantLabel-sc-shj2ft-5")
    LOCATOR_LABORANT_NAME = (By.CLASS_NAME, "LaborantProfileelements__LaborantHeader-sc-shj2ft-1")
    LOCATOR_LABORANT_BIRTHDAY = (By.XPATH, "//label[text()='Дата рождения']")
    LOCATOR_LABORANT_DIRECTION = (By.XPATH, "//label[text()='Направление']")
    LOCATOR_LABORANT_EMAIL = (By.XPATH, "//label[text()='E-mail']")
    LOCATOR_LABORANT_MENTOR = (By.XPATH, "//label[text()='Ментор']")
    LOCATOR_LABORANT_LANGUAGE = (By.XPATH, "//div/div[2]/div[5]/div/label")
    LOCATOR_LABORANT_LOCATION = (By.XPATH, "//label[text()='Локация']")
    LOCATOR_LABORANT_TELEPHONE = (By.XPATH, "//label[text()='Телефон']")
    LOCATOR_LABORANT_SKYPE = (By.XPATH, "//label[text()='Skype']")
    LOCATOR_LABORANT_AWARDS = (By.XPATH, "//label[text()='Награды']")
    LOCATOR_LABORANT_PERSONAL_DATA_HEADER_OF_THE_PAGE = (By.XPATH, "//p[text()='Личный кабинет']")
    LOCATOR_LABORANT_PARTICIPANTS_HEADER_OF_THE_PAGE = (By.XPATH, "//p[text()='Список Участников']")
    LOCATOR_LABORANT_AVATAR = (By.XPATH, "//img[@width='160' and @height='160']")
    LOCATOR_LABORANT_DEPARTAMENT = (
        By.CSS_SELECTOR, ".LaborantProfileelements__LaborantParagraph-sc-shj2ft-6.kXTrcn"
    )
    LOCATOR_LABORANT_LANGUAGE_LEVEL = (By.XPATH, "//div[1]/div/div[2]/div[5]/div/p")
    LOCATOR_LABORANT_DATE_OF_BIRTH = (By.XPATH, "//div/div[2]/div[1]/div[1]/p")
    LOCATOR_LABORANT_TELEPHONE_FORMAT = (By.XPATH, "//div[1]/div/div[2]/div[2]/div[2]/p")

    """
    :: Locators of switchable elements
    """
    LOCATOR_LABORANT_ALL_SWITCHABLE_ELEMENTS = (
        By.CSS_SELECTOR, ".Switcherelements__SwitcherButton-sc-as4453-1"
    )
    LOCATOR_LABORANT_BUTTON_TIMELINE = (By.XPATH, "//div[2]/div[2]/div[2]/div[1]")
    LOCATOR_LABORANT_BUTTON_PROJECT = (By.XPATH, "//div[2]/div[2]/div[2]/div[2]")
    LOCATOR_LABORANT_BUTTON_TIMESHEETS = (By.XPATH, "//div[2]/div[2]/div[2]/div[3]")
    LOCATOR_LABORANT_BUTTON_TASKS = (By.XPATH, "//div[2]/div[2]/div[2]/div[4]")
    LOCATOR_OF_THE_ELEMENTS_OF_THE_PROJECT_TOGGLE_BUTTON = (
        By.CSS_SELECTOR, ".ProjectTableelements__ProjectHeader-sc-iv8bmm-3.KmPXG"
    )
    LOCATOR_LABORANT_SKYPE_LINK = (By.XPATH, "//div[1]/div/div[2]/div[3]/div[2]/a")
    LOCATOR_NUMBER_OF_PARTICIPANTS = (By.XPATH, "//div/table/tbody/tr[2]/td[3]/p")
    LOCATOR_COLUMN_NAME_OF_PARTICIPANTS = (By.XPATH, "//td[text()='ФИ']")
    LOCATOR_NAMES_OF_PARTICIPANTS_IN_THE_PARTICIPANTS_COLUMN = (
        By.CSS_SELECTOR, ".ProjectModalelements__ModalTableRow-sc-ovr6np-9.eskGTT"
    )
    LOCATOR_NAME_OF_THE_DIRECTIONS_COLUMN = (By.XPATH, "//td[text()='Направление']")
    LOCATOR_NAME_OF_THE_DIRECTIONS_IN_THE_COLUMN = (
        By.CSS_SELECTOR, ".ProjectModalelements__ModalTableRow-sc-ovr6np-9.eskGTT"
    )

    """
    :: Locators of the table of the switchable element 'project'
    """
    LOCATOR_LABORANT_PROJECT_PROJECT = (By.XPATH, "//div/table/tbody/tr[1]/td[1]")
    LOCATOR_LABORANT_PROJECT_START_DATE = (By.XPATH, "//div/table/tbody/tr[1]/td[2]")
    LOCATOR_LABORANT_PROJECT_NUMBER_OF_PARTICIPANS = (By.XPATH, "//div/table/tbody/tr[1]/td[3]")
    LOCATOR_LABORANT_PROJECT_PM_PROJECT = (By.XPATH, "//div/table/tbody/tr[1]/td[4]")

    """
    :: Locators for hidden panel elements
    """
    LOCATOR_LABORANT_LOGO_ANDERSEN = (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/img")
    LOCATOR_LABORANT_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//div[1]/ul/li[1]/a/img")
    LOCATOR_LABORANT_LIST_OF_PARTICIPANS = (By.XPATH, "//div[1]/ul/li[2]/a/img")
    LOCATOR_LABORANT_HIDDEN_MENU_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/img")
    LOCATOR_LABORANT_NOTIFICATIONS = (By.XPATH, "//div/div[1]/div[3]/a/img")
    LOCATOR_LABORANT_EXIT_BUTTON = (By.XPATH, "//div/div[1]/div[3]/div[1]/img")
    LOCATOR_LABORANT_HIDDEN_EXIT_BUTTON = (By.XPATH, "//div[3]/div[2]/div")
    LOCATOR_EXIT_CONFIRMATION_BUTTON = (By.XPATH, "//../div[2]/button[2]")
    LOCATOR_EXIT_DENIAL_BUTTON = (By.XPATH, "//../div[2]/button[1]")
    LOCATOR_EXIT_WARNING = (By.XPATH, "//div[1]/div[3]/div[3]/div/div[1]/p")
