from selenium.webdriver.common.by import By


class AuthorizationPageLocators:

    LOCATOR_AUTHORIZATION_PAGE_MAIN_MESSAGE = (By.XPATH, "//h2['Вход в систему']")

    LOCATOR_LOGIN_FIELD = (By.XPATH, "//input[@type='text' and @name='login']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOCATOR_UNCOVER_PASSWORD = (By.XPATH, "//input[@type='password']/../span")
    LOCATOR_ENTER_BUTTON = (By.XPATH, "//button[@type='submit']")
