from Measurement import TruckMeasurement
from .requirement import Requirement
from truck.Truck import Truck

truckRequirements = []

def addTruckRequirement(requirementName, function, errorMessage="No error message added"):
    truckRequirements.append(Requirement(errorMessage, requirementName, function))

    
def hasFrontAxleEnoughWeight(truck: Truck,measurement: TruckMeasurement):
    """
    This function will check if the front axle has at least 20% of the total weight

    Return: true if test pass, false if test fail
    """
    axleWeights = measurement.getMeasuredAxleWeights()
    sum_weight = measurement.getTotalWeight()
    if axleWeights[0]/sum_weight < 0.2:
        return False
    return True
addTruckRequirement("EnoughWeightOnFrontAxle", hasFrontAxleEnoughWeight, "Front axle does not have 20% of total weight")


def exceedsTruckTotalWeight(truck: Truck,measurement: TruckMeasurement):
    totalWeight = measurement.getTotalWeight()
    allowedWeight = truck.getMaxTruckAndTrailerTotalWeight()
    if totalWeight > allowedWeight:
        return False
    return True
addTruckRequirement("TotalWeightNotExceeded", exceedsTruckTotalWeight, "Weight exceeds allowed truck total weight")

def exceedAxleTruckWeight(truck: Truck,measurement: TruckMeasurement):
    axles = truck.getMaxAxleWeights()
    axleWeights = []
    for element in axles:
        axleWeights.append(element[1])
    measuredWeights = measurement.getMeasuredAxleWeights()
    for i in range(len(axleWeights)):
        if axleWeights[i] < measuredWeights[i]:
            return False
    return True
addTruckRequirement("SingleAxleWeightNotExceeded", exceedAxleTruckWeight, "An axle on the truck exceeds allowed weight")

def exceedsAxleTrailerWeight(truck: Truck,measurement: TruckMeasurement):
    axles=truck.trailer.getWeightDistribution()
    measuredWeights = measurement.getMeasuredAxleWeights()[::-1]
    axleWeights = [x[1] for x in axles][::-1]
    for i in range(len(axleWeights)):
        if axleWeights[i] < measuredWeights[i]:
            return False
    return True
addTruckRequirement("TrailerWeightNotExceeded", exceedsAxleTrailerWeight, "An axle on the trailer exceeds allowed weight")





