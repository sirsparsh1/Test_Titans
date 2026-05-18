Feature: Newsletter Subscription

  Scenario: Subscribe using valid email
    Given user opens homepage
    When user subscribes with valid email
    Then subscription should be successful