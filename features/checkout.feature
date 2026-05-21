Feature: Checkout

  Scenario: Checkout order
    Given product already added to cart
    When user proceeds to checkout
    Then order should place successfully