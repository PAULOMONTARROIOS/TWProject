@BasicSearchFlow
Feature: Basic Search Flow


    Background:
        Given the user accesses the MarsAir website

    
    Scenario: T01 - The user can see the "departure" and "return" fields on the form.
        Then the search form presents the standard fields

    
    Scenario: T02 - The user can only schedule half-yearly flights for up to 2 years
        Then the options available will only be July and December until the next 2 years


    Scenario: T03 - The user finds available seats
        When selecting the departure and return that has a seat available
        Then the application should display the message stating availability


    Scenario: T04 - User cannot find seats available
        When selecting the departure and return that does not have a seat available
        Then the application should display a friendly message stating unavailability