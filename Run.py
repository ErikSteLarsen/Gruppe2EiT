#from truck.Truck import Truck
from evaluator import truckRequirements
from Measurement import TruckMeasurement
from truck import Truck

Truck1 = Truck.Truck("kh65201")
Measurement1 = TruckMeasurement(Truck1)

truckRequirements.addAllTruckRequirements()
truckRequirements.truckRequirements[0].testRequirement(Truck1, Measurement1)

lastebil = "DP51062"
henger = "NP5841"
"""
if __name__ == '__main__':
    truck = Truck(lastebil,henger)
    print(truck.getMaxAxelWeights())
    print(truck.trailer.getWeightDistribution())
"""
