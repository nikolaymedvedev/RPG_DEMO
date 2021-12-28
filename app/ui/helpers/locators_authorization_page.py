from selenium.webdriver.common.by import By


class AuthorizationPageLocators:

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


