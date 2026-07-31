import config
from pages.Loginpage import LoginPage
from pages.inventory import InventoryPage
from pages.cartpage import CartPage


class Test_Case07:

    def test_inside_cart(self,driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart=CartPage(driver)
        login.login(config.USERNAME,config.PASSWORD)
        inventory_product=inventory.products_add_to_cart()
        inventory.click_cart_button()
        cart_products=cart.cart_page_product()
        assert inventory_product == cart_products

