
Feature: Delete an event
  User deletes an event

  Background: There is a registered user which has created 3.
    Given Exists a user "user1" with password "password"
    And Exists a team created by "user1"
    | name  | short_name  |
    | team1 | t1          |
    | team2 | t2          |
    | team3 | t3          |
    And Exist a event created by "user1"
    | local | visitor |
    | team1 | team2 |
    | team2 | team3 |
    | team3 | team1 |


    Scenario: User with 3 events deletes one.
      Given I login as user "user1" with password "password"
      When I want to delete the event "team1 v team2"
      And I delete the event
      When I list events
      Then I'm viewing a event list containing
      | local | visitor |
      | team2 | team3 |
      | team3 | team1 |
      
      
    Scenario: User wants to delete an event that he hasn't created
      Given Exists a user "user2" with password "password"
      And I login as user "user2" with password "password"
      When I want to delete the event "team2 v team3"
      Then Server responds with page containing "403"