#include Truck from ../truck
"""
This file include functions for checking that different requirements for the truck axle weights are met

TODO: 
    add more tests
    Add simple interface to use
    Improve Requirement class
    A lot more that i dont see at this moment

"""


class Requirement:
    def __init__(self, function, ErrorMessage):
        self.function = function
        self.ErrorMessage = ErrorMessage

    def testRequirement(self, Truck, Measurement):
        """
        Run test for specified requirement object on Truck object.
        
        Output: Error message if test fail

        Return: True/false based on pass/fail.

        """
        if (self.function(Truck, Measurement)):
            return true
        else
            print(self.ErrorMessage)
            return false

   
