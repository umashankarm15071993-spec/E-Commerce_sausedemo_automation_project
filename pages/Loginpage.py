from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Basepage import BasePage


class LoginPage(BasePage):

    USERNAME_LOC=(By.ID,'user-name')
    PASSWORD_LOC=(By.ID,'password')
    LOGIN_BUTTON=(By.ID,"login-button")
    ERROR_MESSAGE_LOC=(By.TAG_NAME,"h3")

    def __init__(self,driver):
        super().__init__(driver)

    def login(self,user_name,password):
        self.enter_username(user_name)
        self.enter_password(password)
        self.click_login_button()



    def enter_username(self,username):
        element=self.wait.until(EC.visibility_of_element_located(self.USERNAME_LOC))
        element.clear()
        element.send_keys(username or "")

    def enter_password(self,password):
        element=self.wait.until(EC.visibility_of_element_located(self.PASSWORD_LOC))
        element.clear()
        element.send_keys(password or "")

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def get_current_url(self):
        self.geturl()

    def error_message(self):
        element=self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE_LOC)).text
        return element


