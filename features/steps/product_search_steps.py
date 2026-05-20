from behave import given, when, then
from pages.home_page import HomePage
from pages.products_page import ProductsPage


@given('user opens products page')
def open_products(context):
    context.driver.get("https://automationexercise.com/products")
    context.driver.execute_script("""
        document.querySelectorAll('iframe[id^="aswift_"], ins.adsbygoogle').forEach(el => el.remove());
    """)


@when('user searches product "{product}"')
def search_product(context, product):
    ProductsPage(context.driver).search_product(product)


@then('searched product should display')
def verify_product(context):
    assert ProductsPage(context.driver).is_product_visible()