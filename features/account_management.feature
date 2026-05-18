Feature: Account Management

  Scenario: Update account info
    Given user is logged in
    When user updates profile
    Then profile should be updated successfully