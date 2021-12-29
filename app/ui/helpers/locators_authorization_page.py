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
    LOCATOR_BUTTON_LINK = (By.XPATH, "//form/div[3]/span")
    LOCATOR_BUTTON_LINK_HEADING = (By.XPATH, "//form/div/h2")
    LOCATOR_BUTTON_LINK_FIELD = (By.XPATH, "//div/div[2]/label")
    LOCATOR_CHECK_BUTTON = (By.TAG_NAME, "button")
    LOCATOR_CHECK_MAIL_INPUT_FIELD = (By.XPATH, "//input[@name='email']")
    LOCATOR_BUTTON_SEND_EMAIL = (By.XPATH, "//form/div/button")
    LOCATOR_EMAIL_FIELD_NAME = (By.CSS_SELECTOR, ".Inputelements__InputMessage-sc-1fyahir-7.fVxNmY")
