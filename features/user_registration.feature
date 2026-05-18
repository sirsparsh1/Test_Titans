Feature: User Registration

    Background:
        Given the browser is open
        And user navigates to AutomationExercise website

    @smoke @regression
    Scenario: Valid user registration
        Given user opens signup login page
        When user enters valid registration details   
        Then account should be created successfully