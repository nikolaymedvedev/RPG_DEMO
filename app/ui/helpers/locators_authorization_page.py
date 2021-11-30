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
