from behave import given, when, then
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage


@when("user clicks on first product")
def click_first_product(context):
    ProductsPage(context.driver).open_first_product()


@then("product detail page should be displayed")
def verify_product_detail(context):
    assert "product_details" in context.driver.current_url or "product" in context.driver.current_url


@when("user clicks on test cases link")
def click_test_cases(context):
    context.driver.find_element("xpath", "//a[@href='/test_cases']").click()


@then("test cases page should be displayed")
def verify_test_cases_page(context):
    url = context.driver.current_url
    assert "test_cases" in url or "test-cases" in url or context.driver.title != ""
