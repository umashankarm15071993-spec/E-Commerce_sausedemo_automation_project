from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.Basepage import BasePage


class CartPage(BasePage):
    CART_PAGE_PRODUCT_NAME=(By.XPATH,"//div[@class='cart_item_label']/a")
    CART_PAGE_PRODUCT_DESCRIPTION = (By.XPATH, "//div[@data-test='inventory-item-desc']")
    CHECKOUT_BUTTON=(By.ID,"checkout")


    def __init__(self,driver):
        super().__init__(driver)

    def cart_page_product(self):
        products_name=self.wait.until(EC.visibility_of_all_elements_located(self.CART_PAGE_PRODUCT_NAME))
        products_description=self.wait.until(EC.visibility_of_all_elements_located(self.CART_PAGE_PRODUCT_DESCRIPTION))
        cart_product=[]
        for name,description in zip(products_name,products_description):
            cart_product.append({"name":name.text,
                                 "description":description.text})
        return cart_product

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()



