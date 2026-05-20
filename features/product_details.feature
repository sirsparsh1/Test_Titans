Feature: Product Details

  Scenario: View product details
    Given user opens products page
    When user clicks on first product
    Then product detail page should be displayed
