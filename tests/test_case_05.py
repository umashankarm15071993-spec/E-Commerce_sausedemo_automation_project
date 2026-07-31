import config
from pages.Loginpage import LoginPage
from pages.inventory import InventoryPage


class Test_Case05:



    def test_random_product_selection(self,driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        login.login(config.USERNAME, config.PASSWORD)
        products=inventory.random_product_select()
        assert len(products)==4



