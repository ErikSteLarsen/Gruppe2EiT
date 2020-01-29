
import Requirement

truckRequirements = []

def addTruckRequirement(requirementName, errorMessage="No error message added", function):
	truckRequirements.append(Requirement(errorMessage, requirementName, function))

def hasFrontAxleEnoughWeight(Truck, Measurement):
    """
    This function will check if the front axle has at least 20% of the total weight

    Return: True if test pass, false if test fail
    """

"""
---------------------------
The following code add the functions to a Truck Requirements Object
"""
addTruckRequirement(hasFrontAxleEnoughWeight, "FrontAxleWeight20%" ,  "Front axle weight is too low")

