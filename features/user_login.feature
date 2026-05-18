Feature: User Login

  Background:
    Given the browser is open
    And user navigates to AutomationExercise website

  @smoke
  Scenario Outline: Login with credentials
    Given user opens signup login page
    When user enters email "<email>"
    And user enters password "<password>"
    And user clicks login button
    Then user should login successfully

    Examples:
      | email         | password |
      | shaikmusharaf863786@gmail.com | Musharaf@786 |