

from Measurement import TruckMeasurement
import Requirement

truckRequirements = []

def addTruckRequirement(requirementName, function, errorMessage="No error message added"):
	truckRequirements.append(Requirement(errorMessage, requirementName, function))

def hasFrontAxleEnoughWeight(Truck, TruckMeasurement):
    axleWeights = TruckMeasurement.getMeasuredAxleWeights()
    sum_weight = 0
    for weight in axleWeights:
        sum_weight += weight
    if axleWeights[0]/sum_weight < 0.2:
        return False
    return True



    """
    This function will check if the front axle has at least 20% of the total weight

    Return: true if test pass, false if test fail
    """

"""
---------------------------
The following code add the functions to a Truck Requirements Object
"""
addTruckRequirement("EnoughWeightOnFrontAxle", "Front axle does not have 20% of total weight", hasFrontAxleEnoughWeight)