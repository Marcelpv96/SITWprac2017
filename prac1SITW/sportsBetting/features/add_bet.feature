
Feature: User adds a new bet

  Background: Exist a user that will create a bet on a determinate event
    Given Exists a user "user1" with password "password"
    And Exists a user "admin" with password "admin"
    #And Exist a event created by "admin"
    # TODO: Create the event here
    
  Scenario: User creates a bet and looks for it
    Given I login as user "user1" with password "password"
    # When I add a bet
    # TODO: Add the bet based on the previous event
    #And I list bets
    #Then I find a bet with description "test event"
    #And I find a bet with quota "50.00€"