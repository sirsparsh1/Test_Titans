Feature: Invalid Contact Form

  Scenario: Submit contact form with empty fields
    Given user opens contact us page
    When user submits empty contact form
    Then contact form validation should display