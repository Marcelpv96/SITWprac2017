Feature: Add team
  The user wants to add a new team
  in order to create his own event later.

  Background: There is a user registered
    Given Exists a user "user-test" with password "test"


    Scenario: When the user is logged in adds a new team
      Given I login as user "user-test" with password "test"
      When I add a new team
      | name | short_name |
      | Test | FCT        |
      When I list teams filtered by "Test"
      Then I found the team named "Test"



