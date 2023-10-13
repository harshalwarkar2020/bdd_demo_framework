Feature: Outline Calculator Functionality

  @Outline
  Scenario Outline: Addition of number from table
    Given open calculator
    When perform addition on <a> and <b>
    Then sum should be <c>

    Examples: table
    | a | b | c |
    | 2 | 3 | 5 |
    | 4 | 3 | 7 |
    | 4 | 50 | 7 |
