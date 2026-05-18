@api
Feature: Products API

  Scenario: Get all products
    Given products API endpoint
    When user sends GET request
    Then API response status should be 200