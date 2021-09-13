@LinkHomePage
Feature: Link to Home Page


    Background:
        Given the user accesses the MarsAir website


    Scenario: T01 - The MarsAir logo redirects to the home page
        When  selecting the departure, return and inform a valid promotional code
        And   click on the MarsAir logo
        Then  the user will be redirected to the home page