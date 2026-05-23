Feature: Contact Us

  Scenario: Submit contact form
    Given user opens contact us page
    When user submits contact form
    Then success message should display