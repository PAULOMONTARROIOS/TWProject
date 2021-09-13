@PromotionalCodes
Feature: Promotional codes


    Background:
        Given the user accesses the MarsAir website

    
    Scenario: T01 - The user enters a valid promotional code
        When selecting the departure, return and inform a valid promotional code
        Then the application will display a message describing the promotional code
        And  the application of the discount is in accordance with the promotional code

    
    Scenario: T02 - The user enters an invalid promotional code
        When selecting the departure, returning and entering an invalid promotional code
        Then the application will display a message stating that the promotional code is invalid

    @wip
    Scenario: T03 - An accepted promotional code has the valid format
        When selecting the departure, return and inform a valid promotional code
        Then the valid promotional code has the format in the correct pattern



    Scenario: T03 - An accepted promotional code has a valid check digit
        When selecting the departure, return and inform a valid promotional code
        Then the valid promotional code has the correct verifier digit