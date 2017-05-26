
Feature: User edits a competition
  A user who has already registered a new competition is able to edit it.

  Background: There are two users and each one has registered a competition
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists a user "admin" with password "admin"
    And Exists a team created by "admin"
       | name  | short_name |
       | team1 | t1         |
       | team2 | t2         |
       | team3 | t3         |
       | team4 | t4         |
       | team5 | t5         |
    And Exist a competition created by "user1"
      | name         | short_name | teams             |
      | competition1 | c1         | team1,team2,team3 |
    And Exist a competition created by "user2"
      | name         | short_name | teams       |
      | competition2 | c2         | team4,team5 |

  Scenario: User edits his own competition and adds a new team
    Given I login as user "user1" with password "password"
    When I want to edit the competition "competition1"
    And I edit the competition
      | name         | short_name | teams             |
      | competition1 | c1         | team5,team2,team3,team4 |
    And I click to competition "competition1"
    Then I'm viewing a team list containing
      | name  |
      | team2 |
      | team3 |
      | team4 |
      | team5 |
    
    Scenario: User tries to delete a competition that he hasn't created.
      Given I login as user "user1" with password "password"
      When I want to delete the competition "competition2"
      Then Server responds with page containing "403 Forbidden"