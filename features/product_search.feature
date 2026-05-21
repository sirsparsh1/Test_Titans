Feature: Product Search

  Scenario Outline: Search products
    Given user opens products page
    When user searches product "<product>"
    Then searched product should display

    Examples:
      | product  |
      | Blue Top |