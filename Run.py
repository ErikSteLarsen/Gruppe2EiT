#from truck.Truck import Truck
from truck.Truck import Truck
from Measurement import TruckMeasurement
from evaluator.evaluator import Evaluator
from simulator.AdvancedSimulator import AdvancedSimulator

lastebil = "DP51062"
henger = "NP5841"

if __name__ == '__main__':
    truck = Truck(lastebil, henger)
    print(truck.getMaxAxleWeights())
    print(truck.trailer.getWeightDistribution())

    measurement=TruckMeasurement()
    simulator=AdvancedSimulator(truck)
    simulated=simulator.calculateWeights()
    simulated[0]=5500
    measurement.setAxleWeight(simulated)

    results = Evaluator.assert_requirements(truck, measurement)
    print("Results: %a" % results)
