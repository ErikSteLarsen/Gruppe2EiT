from Measurement import TruckMeasurement
from evaluator.requirement  import Requirement

truckRequirements = []

def addTruckRequirement(requirementName, function, errorMessage="No error message added"):
	truckRequirements.append(Requirement(errorMessage, requirementName, function))

def hasFrontAxleEnoughWeight(Truck, TruckMeasurement):
    axleWeights = TruckMeasurement.getMeasuredAxleWeights()
    sum_weight = TruckMeasurement.getTotalWeight()
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
def addAllTruckRequirements():
    print("Adding truck requirements\n")
    addTruckRequirement("EnoughWeightOnFrontAxle",hasFrontAxleEnoughWeight, "Front axle does not have 20% of total weight")
