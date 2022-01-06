from selenium.webdriver.common.by import By


class AuthorizationPageLocators:

    LOCATOR_LOGIN_FIELD = (By.XPATH, "//input[@type='text' and @name='login']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOCATOR_UNCOVER_PASSWORD = (By.XPATH, "//input[@type='password']/../span")
    LOCATOR_ENTER_BUTTON = (By.XPATH, "//button[@type='submit']")

    LOCATOR_ALERT_NOT_VALID_LOGIN = (By.XPATH, "//div/div[2]/form/div[1]/span")
    LOCATOR_ALERT_NOT_VALID_PASSWORD = (By.XPATH, "//span[2][text()='Вы ввели неверный пароль.']")
    LOCATOR_ALERT_REQUIRED_FIELD_LOGIN = (By.XPATH, "//div/span[1][text()='Обязательное поле']")
    LOCATOR_ALERT_REQUIRED_FIELD_PASSWORD = (By.XPATH, "//div/span[2][text()='Обязательное поле']")
    LOCATOR_ALERT_PASSWORD_LENGTH = (By.XPATH, "//div/span[2][text()='Пароль должен содержать 12 символов']")

    LOCATOR_INPUT_FIELDS = (By.TAG_NAME, "input")
    LOCATOR_BUTTON_LINK = (By.XPATH, "//form/div[3]/span")
    LOCATOR_BUTTON_LINK_HEADING = (By.XPATH, "//form/div/h2")
    LOCATOR_BUTTON_LINK_FIELD = (By.XPATH, "//div/div[2]/label")
    LOCATOR_CHECK_BUTTON = (By.TAG_NAME, "button")
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 1248650c60219d60cc311f70d11ef625cc6e1ca1
=======
>>>>>>> ce01e640d418c36e549b5b8a4f02106d5c2d338c
    LOCATOR_CHECK_MAIL_INPUT_FIELD = (By.XPATH, "//input[@name='email']")
    LOCATOR_BUTTON_SEND_EMAIL = (By.XPATH, "//form/div/button")
    LOCATOR_EMAIL_FIELD_NAME = (By.CSS_SELECTOR, ".Inputelements__InputMessage-sc-1fyahir-7.fVxNmY")
    LOCATOR_CROSS_ON_WINDOW_FORGOT_PASSWORD = (By.XPATH,
                                               "//div[@class='WhiteRectangleelements__SVGClose-sc-jonks8-3 hQMJid']"
                                               )
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======


>>>>>>> develop
>>>>>>> 1248650c60219d60cc311f70d11ef625cc6e1ca1
=======
>>>>>>> ce01e640d418c36e549b5b8a4f02106d5c2d338c
