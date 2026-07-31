import random

from pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



class InventoryPage(BasePage):
    BURGER_MENU=(By.ID,"react-burger-menu-btn")
    LOGOUT_BUTTON=(By.XPATH,"//a[text()='Logout']")
    CART_IMAGE=(By.XPATH,"//a[@data-test='shopping-cart-link']")
    TOTAL_INVENTORY_LIST=(By.XPATH,"inventory-list")
    PRODUCT_NAME=(By.XPATH,"//div[@class='inventory_item_description']//descendant::a")
    PRODUCT_PRICE=(By.XPATH,"//div[@class='pricebar']//div")
    ADD_CART=(By.XPATH,"//div[@class='pricebar']//button")
    PRODUCT1=(By.XPATH,"//div[normalize-space()='Sauce Labs Backpack']/ancestor::div[@data-test='inventory-item-description']/descendant::button[@id='add-to-cart-sauce-labs-backpack']")
    PRODUCT2=(By.XPATH,"//div[normalize-space()='Sauce Labs Bike Light']/ancestor::div[@data-test='inventory-item-description']/descendant::button")
    PRODUCT_DESCRIPTION=(By.XPATH,"//div[@data-test='inventory-item-desc']")
    Drop_Down=(By.TAG_NAME,'select')
    APP_RESET_STATE=(By.XPATH,"//a[normalize-space()='Reset App State']")



    def __init__(self,driver):
        super().__init__(driver)


    def click_menu(self):
        self.wait.until(EC.visibility_of_element_located(self.BURGER_MENU)).click()

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()

    def is_logout_visible(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def cart_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_IMAGE))

    def cart_enable(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_IMAGE))

    def random_product_select(self):
        products=self.driver.find_elements(*self.PRODUCT_NAME)
        price=self.driver.find_elements(*self.PRODUCT_PRICE)
        random_list=random.sample(range(len(products)),4)
        selected_product=[]
        for index in random_list:
            selected_product.append({"name":products[index].text,
                                    "price":price[index].text})
        print(selected_product)
        return selected_product

    def product_add_cart(self):
        products=self.driver.find_elements(*self.PRODUCT_NAME)
        price=self.driver.find_elements(*self.PRODUCT_PRICE)
        add_cart=self.driver.find_elements(*self.ADD_CART)

        random_list=random.sample(range(len(products)),4)
        selected_product=[]
        for index in random_list:
            selected_product.append({"name":products[index].text,
                                    "price":price[index].text})
            add_cart[index].click()


        return selected_product

    def get_cart_count(self):
        element=self.driver.find_element(*self.CART_IMAGE)
        return element.text

    def get_product_description(self):
        element=self.driver.find_element(*self.PRODUCT_DESCRIPTION)
        return element.text


    def products_add_to_cart(self):
        products = self.driver.find_elements(*self.PRODUCT_NAME)
        description= self.driver.find_elements(*self.PRODUCT_DESCRIPTION)
        add_cart = self.driver.find_elements(*self.ADD_CART)

        random_list = random.sample(range(len(products)), 2)
        selected_product = []
        for index in random_list:
            selected_product.append({"name": products[index].text,
                                     "description": description[index].text})
            add_cart[index].click()

        return selected_product

    def click_cart_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_IMAGE)).click()

    def descending_order(self):
        select=Select(self.driver.find_element(*self.Drop_Down))
        select.select_by_visible_text("Name (Z to A)")

    def get_products_name(self):
        products=self.driver.find_elements(*self.PRODUCT_NAME)
        return [product.text for product in products]

    def price_filter(self):
        select=Select(self.driver.find_element(*self.Drop_Down))
        select.select_by_value("hilo")

    def price_sort_product(self):
        prices=self.driver.find_elements(*self.PRODUCT_PRICE)
        return [float(price.text.replace("$",""))for price in prices]

    def click_app_reset_button(self):
        self.wait.until(EC.element_to_be_clickable(self.APP_RESET_STATE)).click()

    def get_button_state(self):
        add_cart_buttons=self.driver.find_elements(*self.ADD_CART)
        return [button.text for button in add_cart_buttons]

