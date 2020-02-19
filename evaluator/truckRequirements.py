from Measurement import TruckMeasurement
from .requirement import Requirement
from truck.Truck import Truck

truckRequirements = []

def addTruckRequirement(requirementName, function, errorMessage="No error message added"):
    truckRequirements.append(Requirement(errorMessage, requirementName, function))

    
def hasFrontAxleEnoughWeight(truck: Truck,measurement: TruckMeasurement):
    """
    This function checks if the front axle has at least 20% of the total weight.

    :param truck:
    :param measurement:
    :return: true if more than 20% of the totalweight is on the front axle, false if not
    """
    axleWeights = measurement.getMeasuredAxleWeights()
    sum_weight = measurement.getTotalWeight()
    if axleWeights[0]/sum_weight < 0.2:
        return False
    return True
addTruckRequirement("EnoughWeightOnFrontAxle", hasFrontAxleEnoughWeight, "Front axle does not have 20% of total weight")


def exceedsTruckTotalWeight(truck: Truck,measurement: TruckMeasurement):
    """
    This function checks whether or not the measured total weight exceeds the maximum allowed weight.

    :param truck:
    :param measurement:
    :return: true if measured total weight is less than allowed, false if more than allowed.
    """
    totalWeight = measurement.getTotalWeight()
    allowedWeight = truck.getMaxTruckAndTrailerTotalWeight()
    if totalWeight > allowedWeight:
        return False
    return True
addTruckRequirement("TotalWeightNotExceeded", exceedsTruckTotalWeight, "Weight exceeds allowed truck total weight")


def exceedAxleTruckWeight(truck: Truck,measurement: TruckMeasurement):
    """
    This function checks if AT LEAST ONE of the axles on the TRUCK exceeds their maximum allowed weight.

    :param truck:
    :param measurement:
    :return: true if none of the axles on TRUCK has more weight than allowed, false if one of them does.
    """
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
    """
    This function checks if AT LEAST ONE of the axles on the TRAILER exceeds their maximum allowed weight.

    :param truck: used to access the trucks connected TRAILER object.
    :param measurement:
    :return: true if none of the axles on the TRAILER has exceeds weight, false if one does.
    """
    axles=truck.trailer.getWeightDistribution()
    measuredWeights = measurement.getMeasuredAxleWeights()[::-1]
    axleWeights = [x[1] for x in axles][::-1]
    for i in range(len(axleWeights)):
        if axleWeights[i] < measuredWeights[i]:
            return False
    return True
addTruckRequirement("TrailerWeightNotExceeded", exceedsAxleTrailerWeight, "An axle on the trailer exceeds allowed weight")





