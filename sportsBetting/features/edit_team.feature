Feature: Edit a team
  Edit a team because when it was created there was an error.


  Background: There is a user registered
    Given Exists a user "user1" with password "password"
    And Exists a team created by "user1"
    | name  | short_name  |
    | error | fce         |
    And Exists a user "user2" with password "password"
    And Exists a team created by "user2"
      | name      | short_name  |
      | user2Team | u2t         |


  Scenario: User edits team and search it
    Given I login as user "user1" with password "password"
    When I want to edit the team "error"
    And I edit the team
      | name    | short_name  |
      | correct | fcc         |
    And I list teams filtered by "correct"
    Then I found the team named "correct"


  Scenario: User tries to edit a team that he hasn't created
    Given I login as user "user1" with password "password"
    When I want to edit the team "user2Team"
    Then Server responds with page containing "403 Forbidden"
