#from truck.Truck import Truck
from evaluator import truckRequirements
from Measurement import TruckMeasurement
from truck import Truck
from simulator import Simulator

Truck1 = Truck.Truck("kh65201")
Measurement1 = TruckMeasurement()

#truckRequirements.addAllTruckRequirements()
#truckRequirements.truckRequirements[0].testRequirement(Truck1, Measurement1)

lastebil = "DP51062"
henger = "NP5841"

truck=Truck.Truck(lastebil,henger)
measurement=TruckMeasurement()
simulator=Simulator.Simulator(truck)
simulated=simulator.calculateWeights()
simulated[0]=5500
measurement.setAxleWeight(simulated)
truckRequirements.addAllTruckRequirements()
truckRequirements.truckRequirements[0].testRequirement(truck, measurement)
