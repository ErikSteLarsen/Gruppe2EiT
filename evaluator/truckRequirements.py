
from Measurement import TruckMeasurement
from .requirement import Requirement

truckRequirements = []

def addTruckRequirement(requirementName, function, errorMessage="No error message added"):
    truckRequirements.append(Requirement(errorMessage, requirementName, function))



"""
    This function will check if the front axle has at least 20% of the total weight

    Return: true if test pass, false if test fail
    """
def hasFrontAxleEnoughWeight(Truck, TruckMeasurement):
    axleWeights = TruckMeasurement.getMeasuredAxleWeights()
    sum_weight = TruckMeasurement.getTotalWeight() 
    if axleWeights[0]/sum_weight < 0.2:
        return False
    return True
addTruckRequirement("EnoughWeightOnFrontAxle", hasFrontAxleEnoughWeight, "Front axle does not have 20% of total weight")


def exceedsTotalWeight(Truck, TruckMeasurement):
    totalWeight = TruckMeasurement.getTotalWeight()
    allowedWeight = Truck.getMaxTotalWeight()
    if totalWeight > allowedWeight:
        return False
    return True
addTruckRequirement("TotalWeightNotExceeded", exceedsTotalWeight, "Weight exceeds allowed total weight")

def exceedWeightOnOneOfAxels(Truck, TruckMeasurement):
    axels = Truck.getMaxAxelWeights()
    axelWeights = []
    for element in axels:
        axelWeights.append(element[1])
    measuredWeights = TruckMeasurement.getMeasuredAxleWeights()
    for i in range(len(axelWeights)):
        if axelWeights[i] < measuredWeights[i]:
            return False
    return True
addTruckRequirement("SingleAxleWeightNotExceeded", exceedWeightOnOneOfAxels, "An axle exceeds allowed weight")




