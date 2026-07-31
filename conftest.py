from selenium import webdriver
import config
import pytest
from selenium.webdriver.chrome.options import Options



chrome_option = Options()
prefs = {
    "credentials_enable_service": False,
        "profile.password_manager_enabled": False
        }
chrome_option.add_experimental_option("prefs", prefs)
chrome_option.add_argument("--disable-notifications")
chrome_option.add_argument("--ignore-certificate-errors")
chrome_option.add_argument("--disable-popup-blocking")
chrome_option.add_argument("--disable-save-password-bubble")
chrome_option.add_argument("--guest")

@pytest.fixture(scope="function")
def driver():
    driver=webdriver.Chrome(options=chrome_option)
    driver.maximize_window()
    driver.get(config.Baseurl)
    yield driver
    driver.quit()
