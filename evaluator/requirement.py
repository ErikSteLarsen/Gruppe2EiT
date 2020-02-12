"""
This file include functions for checking that different requirements for the truck axle weights are met

TODO: 
    add more tests
    Add simple interface to use
    Improve Requirement class
    A lot more that i dont see at this moment

"""


class Requirement:
    def __init__(self, errorMessage, requirementName, function):
        self.function = function
        self.errorMessage = errorMessage
        self.requirementName = requirementName

    def testRequirement(self, truck, measurement):
        """
        Run test for specified requirement object on Truck object.
        
        Output: Error message if test fail

        Return: True/false based on pass/fail.

        """

        if (self.function(truck, measurement)):
            return True
        else:
            print(self.errorMessage)
            return False
