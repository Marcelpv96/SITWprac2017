
Feature: User adds new competitions
  User adds new competitions with some teams in it.

  Background:
    Given Exists a user "user1" with password "password"
    And Exists a team created by "user1"
    | name  | short_name |
    | team1 | t1         |
    | team2 | t2         |
    | team3 | t3         |
    | team4 | t4         |
    | team5 | t5         |
    And Exist a competition created by "user1"
      | name   | short_name | teams             |
      | 3teams | 3t         | team1,team2,team3 |
    And Exists a user "user2" with password "password"


  Scenario: Adding competition test and search for it
    Given I login as user "user1" with password "password"
    When I add a new competition
      | name              | short_name | teams                          |
      | Test-Competition  | TC         | team1,team2,team3,team4,team5  |
    And I list competitions filtered by "Test-Competition"
    Then I found the competition named "Test-Competition"


  Scenario: User clicks to a 3teams competition and all 3teams teams are listed
    Given I login as user "user1" with password "password"
    When I click to competition "3teams"
    Then I'm viewing a team list containing
      | name    |
      | team1   |
      | team2   |
      | team3   |