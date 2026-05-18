Feature: Product Review

  Scenario: Submit product review
    Given user opens product page
    When user submits review
    Then review success message should appear