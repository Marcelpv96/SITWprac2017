Feature: Add team
  The user wants to add a new team
  in order to create his own event later.

  Background: There is a user registered
    Given Exists a user "hola" with password "pass"
    And Exists a user "user2" with password "pass"
    And Exists a team created by "user2"
    | name      | short_name  |
    | user2Team | u2t         |


    Scenario: When the user is logged in, adds a new team
      Given I login as user "hola" with password "1234"
      When I add a new team
      | name | short_name |
      | Test | FCT        |
      When I list teams filtered by "Test"
      Then I found the team named "Test"


    Scenario: User tries to edit a team that he hasn't created
      Given I login as user "hola" with password "pass"
      When I edit the team "user2Team"
      Then Server responds with page containing "403 Forbidden"





