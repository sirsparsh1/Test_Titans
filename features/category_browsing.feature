Feature: Category Browsing

  Background:
    Given the browser is open
    And user navigates to AutomationExercise website

  @regression
  Scenario: Browse Women category
    Given user opens category section
    When user selects Women category
    Then category products should be displayed