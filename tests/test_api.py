from utils.api_helper import APIHelper


def test_get_products_api():

    url = "https://automationexercise.com/api/productsList"

    response = APIHelper.get_request(url)

    assert response.status_code == 200