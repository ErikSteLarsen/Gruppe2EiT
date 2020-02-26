from Measurement import TruckMeasurement
from .requirement import Requirement
from truck.Truck import Truck
from truck.Boogie import Boogies
from truck.Boogie import Boogie

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


def getRoadStandardIndex(boogie: Boogie):
    
    if (len(boogie.boogieWheels) == 1):
        if(boogie.driveShaft == True):
            return 1
        else: 
            return 0
    elif (len(boogie.boogieWheels) == 2):
        if (boogie.axleDistance < 800):
            return 5
        elif (boogie.axleDistance < 1200):
            return 4
        elif (boogie.axleDistance < 1300):
            return 3
        else:
            return 2
    elif (len(boogie.boogieWheels) == 3):
        if (boogie.axleDistance < 1000):
            return 8
        elif (boogie.axleDistance < 1300):
            return 7
        else:
            return 6
    else:
        print("Boogie Wheels is" + str(boogie.boogieWheels))

def followRoadRegulations(truck: Truck,measurement: TruckMeasurement):
    """
    Checks if Axle boogie weights are within road regulations for specified road.
    """
   # print("Velg veistandard:\n\t1) Bk6\n\t2) Bk8 \n\t3) BkT8 \n\t4) BK10")
   # roadType = input()
    roadStandards = []
    roadStandards.append([10000, 11500, 18000, 16000, 15000, 10000, 24000, 22000, 16000])#Bk10
    roadStandards.append([8000, 8000, 14000, 12000, 11500, 8000, 19000, 18000, 12000])#BkT8
    roadStandards.append([8000, 8000, 12000, 12000, 11500, 8000, 16000, 16000, 12000])#Bk8
    roadStandards.append([6000, 6000, 9000, 9000, 8500, 6000, 12000, 12000, 9000])#Bk6
    
    wheelIndex = 0
    axleWeights = measurement.getMeasuredAxleWeights()
    boogieWeights = []
    for boogie in truck.boogies.getBoogies():
        sum = 0
        for axle in boogie.boogieWheels:
        sum += measurement.getMeasuredAxleWeights()[axle]
        boogieWeights.append(sum)

    for r in range(len(roadStandards)):
        for i in range(len(boogieWeights)):
            if(boogieWeights[i] > roadStandards[r][getRoadStandardIndex(truck.boogies.getBoogies()[i])]):
                return False #fail on road index r
    return True

addTruckRequirement("Does not follow Road Regulation", followRoadRegulations, "To high boogie weight for road")

        










