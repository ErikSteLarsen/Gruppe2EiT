#from truck.Truck import Truck
from truck.Truck import Truck
from Measurement import TruckMeasurement
from evaluator.evaluator import assert_requirements
from simulator.AdvancedSimulator import AdvancedSimulator
from simulator.Simulator import Simulator

lastebil = "DP51062"
henger = "NP5841"

if __name__ == '__main__':
    testTruck = Truck(lastebil, henger)
    print(testTruck.getMaxAxleWeights())
    print(testTruck.trailer.getWeightDistribution())

    measurement=TruckMeasurement()
    #For å bytte simulator trengs det bare å legges til/fjerne Advanced før Simulator
    simulator=AdvancedSimulator(testTruck)
    simulated=simulator.calculateWeights(5500)
    measurement.setAxleWeight(simulated)

    results = assert_requirements(testTruck, measurement)
    print("Results: %a" % results)
