@InvalidReturnDates
Feature: Invalid Return Dates


    Background:
        Given the user accesses the MarsAir website


    Scenario: T01 - The user is unable to search for a trip with a return of less than 1 year
        When selecting departure and return less than 1 year apart
        Then the application should display the friendly message stating that the schedule is unavailable