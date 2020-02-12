#from truck.Truck import Truck
from truck.Truck import Truck
from Measurement import TruckMeasurement
from evaluator.evaluator import assert_requirements
from simulator.AdvancedSimulator import AdvancedSimulator

lastebil = "DP51062"
henger = "NP5841"

if __name__ == '__main__':
    testTruck = Truck(lastebil, henger)
    print(testTruck.getMaxAxleWeights())
    print(testTruck.trailer.getWeightDistribution())

    measurement=TruckMeasurement()
    simulator=AdvancedSimulator(testTruck)
    simulated=simulator.calculateWeights()
    simulated[0]=5500
    print(simulated)
    measurement.setAxleWeight(simulated)

    results = assert_requirements(testTruck, measurement)
    print("Results: %a" % results)
