from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config


class BasePage:

    def __init__(self,driver):
      self.driver=driver
      self.wait=WebDriverWait(driver,config.EXPLICITWAIT,poll_frequency=2)

    def geturl(self):
        return self.driver.current_url

    def alert(self):
        self.driver.switch_to.alert.accept()
