Feature: Empty Product Search

  Scenario: Search product without entering value
    Given user opens products page
    When user searches with empty value
    Then product search should fail