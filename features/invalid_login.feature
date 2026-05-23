Feature: Invalid Login

  Scenario: Login with invalid credentials
    Given user opens login page
    When user enters invalid email and password
    And user clicks login button
    Then error message should display