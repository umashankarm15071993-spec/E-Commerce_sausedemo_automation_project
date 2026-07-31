import config
from pages.Loginpage import LoginPage
from pages.inventory import InventoryPage


class Test_Case06:

    def test_verify_add_cart_product(self,driver):
            login = LoginPage(driver)
            inventory = InventoryPage(driver)
            login.login(config.USERNAME, config.PASSWORD)
            products=inventory.product_add_cart()
            assert len(products)== 4
            assert inventory.get_cart_count() == "4"
