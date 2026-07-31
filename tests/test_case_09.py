import config
from pages.Loginpage import LoginPage
from pages.inventory import InventoryPage


class Test_Case09:
    def test_verify_sort_dd(self,driver):
        login=LoginPage(driver)
        inventory=InventoryPage(driver)
        login.login(config.USERNAME,config.PASSWORD)
        inventory.descending_order()
        actual=inventory.get_products_name()
        expected = sorted(actual,reverse=True)
        assert actual == expected
        inventory.price_filter()
        actual = inventory.price_sort_product()
        expected = sorted(actual, reverse=True)
        assert actual == expected



