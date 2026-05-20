Feature: Category Browsing

  Scenario: Browse products by category
    Given user opens homepage
    When user selects category "Women" and subcategory "Dress"
    Then category products should be displayed
