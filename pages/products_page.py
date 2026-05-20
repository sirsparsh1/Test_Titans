from selenium.webdriver.common.by import By
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

    SEARCH_BOX = (
        By.ID,
        "search_product"
    )

    SEARCH_BTN = (
        By.ID,
        "submit_search"
    )

    PRODUCT_LIST = (
        By.XPATH,
        "//div[@class='productinfo text-center']"
    )

    SEARCHED_PRODUCT = (
        By.XPATH,
        "//*[contains(text(),'Blue Top')]"
    )

    ADD_TO_CART_BTN = (
        By.XPATH,
        "(//a[@data-product-id])[1]"
    )

    CONTINUE_SHOPPING = (
        By.XPATH,
        "//button[contains(text(),'Continue Shopping')]"
    )

    BRAND_PRODUCTS = (
        By.XPATH,
        "//h2[contains(text(),'Brand -')]"
    )

    def open_products_page(self):

        self.driver.get(
            "https://automationexercise.com/products"
        )

        self.wait_for_page_load()

    def search_product(self, product):

        self.enter_text(
            self.SEARCH_BOX,
            product
        )

        self.click(
            self.SEARCH_BTN
        )

    def is_product_visible(self):

        products = self.driver.find_elements(
            *self.PRODUCT_LIST
        )

        return len(products) > 0

    def is_searched_product_displayed(self):

        return self.is_visible(
            self.SEARCHED_PRODUCT
        )

    def open_first_product(self):

        self.click(
            self.FIRST_PRODUCT
        )

    def add_first_product_to_cart(self):

        self._remove_ads()

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_TO_CART_BTN
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        try:

            continue_btn = self.wait.until(
                EC.element_to_be_clickable(
                    self.CONTINUE_SHOPPING
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                continue_btn
            )

        except:
            pass

    def select_brand(self, brand):
        self._remove_ads()

        self.wait_for_page_load()

        brand_xpath = (
        By.XPATH,
        f"//a[@href='/brand_products/{brand}']"
         )

        element = self.wait.until(
        EC.presence_of_element_located(
            brand_xpath
        )
        )

        self.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        element
        )

        self.wait.until(
        EC.element_to_be_clickable(
            brand_xpath
        )
        )

        self.driver.execute_script(
        "arguments[0].click();",
        element
        )

        self.wait_for_page_load()

    def is_brand_page_displayed(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.BRAND_PRODUCTS
            )
        ).is_displayed()

    def _remove_ads(self):

        self.driver.execute_script("""
            document.querySelectorAll('iframe').forEach(
                e => e.remove()
            );
        """)