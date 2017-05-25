
Feature: User adds a new bet

  Background: Exist a user that will create a bet on a determinate event
    Given Exists a user "admin" with password "admin"
    And Exists a user "user1" with password "password"
    And Exists a team created by "admin"
    | name | short_name |
    | team1 | t1        |
    | team2 | t2        |
    And Exist a event created by "admin"
    | local | visitor |
    | team1 | team2   |
    
  Scenario: User creates a bet and looks for it
    Given I login as user "user1" with password "password"
    When I add a bet on "team1 v team2"
    | description | quota |
    | Team1 wins. | 10.5  |
    And I list bets
    Then I find a bet with description "Team1 wins."
    And I find a bet with quota "10.50€"