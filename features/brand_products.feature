Feature: Brand Products

  Scenario: View products by brand
    Given user opens products page
    When user selects brand "POLO"
    Then brand products should be displayed