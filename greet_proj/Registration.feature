Feature: Verifiying Registartion Functionality


  Background:
    Given : User is on Registration page

  @sanity
  Scenario: Registration with valid data
    When : User entered username
    And : User entered email id
    And : User entered password
    And : User click on signup button
    Then : User should be registered successfully

  @sanity @smoke
  Scenario: Registration with valid second data
    When : User entered username
    And : User entered email id
    And : User entered password

  @abcd
  Scenario: Registration with valid third data
    When : User entered username
    And : User entered email id
    And : User entered password