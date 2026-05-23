Feature: Wishlist and Remove

  Scenario: Add and remove product
    Given user adds product to cart
    When user removes product from cart
    Then cart should be empty