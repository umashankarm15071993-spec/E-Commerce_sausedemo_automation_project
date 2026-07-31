import config
from pages.Loginpage import LoginPage
from pages.inventory import InventoryPage


class Test_Case04:

    def test_verify_cart_icon(self,driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        login.login(config.USERNAME, config.PASSWORD)
        assert inventory.cart_visible().is_displayed()
        assert  inventory.cart_enable().is_enabled()
