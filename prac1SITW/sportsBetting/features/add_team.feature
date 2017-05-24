Feature: Add team
  The user wants to add a new team
  in order to create his own event later.

  Background: There is a user registered
    Given Exists a user "user1" with password "password"


    Scenario: When the user is logged in, adds a new team
      Given I login as user "user1" with password "password"
      When I add a new team
      | name | short_name |
      | Test | FCT        |
      When I list teams filtered by "Test"
      Then I found the team named "Test"


    Scenario: User which is not logged in tires to add a team
      Given I'm not logged in
      When I add a new team
      | name | short_name |
      | Test | FCT        |
      Then I'm redirected to the login page




