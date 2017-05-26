Feature: Add event
  User adds an event in order to other users can bet on it.

  Background: There is a user registered
    Given Exists a user "user1" with password "password"
    And Exists a team created by "user1"
    | name  | short_name |
    | team1 | t1         |
    | team2 | t2         |


    Scenario: When the user is logged in, adds a new event
      Given I login as user "user1" with password "password"
      When I add a new event
      | local | visitor |
      | team1 | team2   |
      And I list "team1" events
      Then I find a event named "team1 v team2"
