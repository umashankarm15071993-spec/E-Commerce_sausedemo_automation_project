from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.Basepage import BasePage


class Checkout(BasePage):

    FIRSTNAME=(By.ID,'first-name')
    LASTNAME=(By.ID,'last-name')
    ZIPCODE=(By.ID,'postal-code')
    CONTINUE=(By.ID,'continue')
    FINISH=(By.ID,'finish')
    COMPLETE=(By.TAG_NAME,'h2')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_firstname(self):
        self.wait.until(EC.presence_of_element_located(self.FIRSTNAME)).send_keys('uma')

    def enter_lastname(self):
        self.wait.until(EC.presence_of_element_located(self.LASTNAME)).send_keys('shankar')

    def enter_zipcode(self):
        self.wait.until(EC.presence_of_element_located(self.ZIPCODE)).send_keys('12345')


    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()
        self.driver.save_screenshot('checkout_summary.png')

    def click_finsh(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH)).click()

    def success_message(self):
        return self.wait.until(EC.presence_of_element_located(self.COMPLETE)).text

    def checkout(self):
        self.enter_firstname()
        self.enter_lastname()
        self.enter_zipcode()
        self.click_continue()
        self.click_finsh()
