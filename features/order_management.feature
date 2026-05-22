Feature: Order Management

  Scenario: Verify order history
    Given user has placed an order
    When user opens order history
    Then order should be displayed