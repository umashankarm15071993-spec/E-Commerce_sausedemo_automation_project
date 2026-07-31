import config
from pages.Loginpage import LoginPage
from pages.inventory import InventoryPage


class Test_Case03:

    def test_verify_logout(self,driver):
        login=LoginPage(driver)
        inventory=InventoryPage(driver)
        login.login(config.USERNAME,config.PASSWORD)
        inventory.click_menu()
        inventory.click_logout()
        assert "inventory" not in driver.current_url
