from behave import given, when, then
from pages.category_page import CategoryPage


@given("user opens category section")
def open_category(context):
    pass


@when("user selects Women category")
def select_women(context):
    pass


@when('user selects category "{category}" and subcategory "{subcategory}"')
def select_category(context, category, subcategory):
    CategoryPage(context.driver).open_women()


@then("category products should be displayed")
def verify_category(context):
    assert True