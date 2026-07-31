import config
from pages.Loginpage import LoginPage
from pages.inventory import InventoryPage


class test_case10:

    def test_app_reset(self,driver):
        loginpage=LoginPage(driver)
        inventorypage=InventoryPage(driver)
        loginpage.login(config.USERNAME,config.PASSWORD)
        inventorypage.products_add_to_cart()
        assert all(button == "Remove" for button in inventorypage.get_button_state())
        inventorypage.click_menu()
        inventorypage.click_app_reset_button()
        inventorypage.get_button_state()
        assert all(button == "Add to cart" for button in inventorypage.get_button_state())