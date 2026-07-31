import time

import config
from pages.Loginpage import LoginPage
from pages.cartpage import CartPage
from pages.inventory import InventoryPage
from pages.checkout import Checkout


class Test_Case08:

    def test_verify_checkout(self,driver):
        login=LoginPage(driver)
        inventory=InventoryPage(driver)
        cart=CartPage(driver)
        checkout=Checkout(driver)
        login.login(config.USERNAME,config.PASSWORD)
        inventory.products_add_to_cart()
        inventory.click_cart_button()
        cart.click_checkout()
        checkout.checkout()
        assert "Thank you" in checkout.success_message()

