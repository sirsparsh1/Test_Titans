Feature: Product Details

  Background:
    Given the browser is open
    And user navigates to AutomationExercise website

  @smoke
  Scenario: View product details
    Given user opens products page
    When user selects first product
    Then product details should be visible