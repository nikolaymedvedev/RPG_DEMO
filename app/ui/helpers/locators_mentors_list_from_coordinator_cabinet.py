from selenium.webdriver.common.by import By


class MentorsListLocators:

    LOCATOR_SEARCH_INPUT = (By.CSS_SELECTOR, "[action='search']")
    LOCATOR_DIRECTIONS_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Выберете направление')]")
    LOCATOR_DIRECTIONS_DEV = (By.XPATH, "//div[2]/div[1]/input")
    LOCATOR_DIRECTIONS_QA = (By.XPATH, "//div[2]/div[2]/input")
    LOCATOR_DIRECTIONS_BA = (By.XPATH, "//div[2]/div[3]/input")
    LOCATOR_DIRECTIONS_UX_UI = (By.XPATH, "//div[2]/div[4]/input")
    LOCATOR_DIRECTIONS_PM = (By.XPATH, "//div[2]/div[5]/input")
    LOCATOR_DIRECTIONS_DEVOPS = (By.XPATH, "//div[2]/div[6]/input")
    LOCATOR_DIRECTIONS_SYSADMIN = (By.XPATH, "//div[2]/div[7]/input")
    LOCATOR_APPLY_BUTTON = (By.XPATH, "//button[text()='Применить']")

    LOCATOR_ADD_MENTOR_BUTTON = (By.XPATH, "//button[text()='Добавить ментора']")
    LOCATOR_ADD_MENTOR_BUTTON_ADD = (By.XPATH, "//button[text()='Добавить']")
    LOCATOR_ADD_MENTOR_BUTTON_CANCEL = (By.XPATH, "//button[text()='Отмена']")

    LOCATOR_SHOW_BY_20 = (By.XPATH, "//div[contains(text(),'20')]")
    LOCATOR_SHOW_BY_40 = (By.XPATH, "//div[contains(text(),'40')]")
    LOCATOR_SHOW_BY_60 = (By.XPATH, "//div[contains(text(),'60')]")

    LOCATOR_PAGE_1 = (By.XPATH, "//div[text()='1']")
    LOCATOR_PAGE_2 = (By.XPATH, "//div[text()='2']")
    LOCATOR_PAGE_3 = (By.XPATH, "//div[text()='3']")
    LOCATOR_PAGE_PREVIOUS = (By.XPATH, "//div[@class='PaginationButtonelements__PaginationButtonWrapper-sc-1r99058-0 "
                                       "FZTxd']")
    LOCATOR_PAGE_NEXT = (By.XPATH, "//div[@class='PaginationButtonelements__PaginationButtonWrapper-sc-1r99058-0 "
                                   "kecsNf']")

    LOCATOR_MY_PROFILE = (By.XPATH, "//img[@src='/icons/img.png']")
    LOCATOR_QUIT_BUTTON = (By.XPATH, "//div[text()='Выйти']")
    LOCATOR_QUIT_BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    LOCATOR_QUIT_BUTTON_NO = (By.XPATH, "//button[text()='Нет']")

