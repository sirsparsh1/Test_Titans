Feature: Shopping Cart

  Scenario: Add product to cart
    Given user opens products page
    When user adds product to cart
    Then product should be visible in cart