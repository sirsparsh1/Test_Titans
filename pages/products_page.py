from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
class ProductsPage(BasePage):

    PRODUCTS_LINK = (
        By.XPATH,
        "//a[@href='/products']"
    )

    FIRST_PRODUCT = (
        By.XPATH,
        "(//a[contains(text(),'View Product')])[1]"
    )

    SEARCH_BOX = (By.ID, "search_product")

    SEARCH_BTN = (By.ID, "submit_search")

    PRODUCT_LIST = (
        By.XPATH,
        "//div[@class='productinfo text-center']"
    )

    ADD_TO_CART_BTN = (
        By.XPATH,
        "(//a[@data-product-id])[1]"
    )

    CONTINUE_SHOPPING = (
        By.XPATH,
        "//button[contains(text(),'Continue Shopping')]"
    )

    # ✅ BRAND PAGE TITLE
    BRAND_PRODUCTS = (
        By.XPATH,
        "//h2[contains(text(),'Brand -')]"
    )

    # =========================
    # OPEN PRODUCTS PAGE
    # =========================
    def open_products_page(self):

        self.wait_for_page_load()

        self.click(self.PRODUCTS_LINK)

    # =========================
    # SEARCH PRODUCT
    # =========================
    def search_product(self, product):

        self.enter_text(self.SEARCH_BOX, product)

        self.click(self.SEARCH_BTN)

    # =========================
    # VERIFY PRODUCT VISIBLE
    # =========================
    def is_product_visible(self):

        products = self.driver.find_elements(*self.PRODUCT_LIST)

        return len(products) > 0

    # =========================
    # OPEN FIRST PRODUCT
    # =========================
    def open_first_product(self):

        self.click(self.FIRST_PRODUCT)

    # =========================
    # ADD PRODUCT TO CART
    # =========================
    def add_first_product_to_cart(self):

        self.click(self.ADD_TO_CART_BTN)

        try:
            self.click(self.CONTINUE_SHOPPING)
        except:
            pass

    # =========================
    # SELECT BRAND
    # =========================
    def select_brand(self, brand):
        brand_xpath = (
            By.XPATH,
            f"//div[@class='brands_products']//a[contains(., '{brand}')]"
        )
        self.click(brand_xpath)

    # =========================
    # VERIFY BRAND PAGE
    # =========================
    def is_brand_page_displayed(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.BRAND_PRODUCTS
            )
        )
            return element.is_displayed()
        except:
            return False