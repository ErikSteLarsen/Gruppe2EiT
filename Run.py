#from truck.Truck import Truck
from truck.Truck import Truck
from Measurement import TruckMeasurement
from evaluator.evaluator import Evaluator
from simulator.Simulator import Simulator

lastebil = "DP51062"
henger = "NP5841"

if __name__ == '__main__':
    truck = Truck(lastebil, henger)
    print(truck.getMaxAxelWeights())
    print(truck.trailer.getWeightDistribution())

    measurement=TruckMeasurement()
    simulator=Simulator(truck)
    simulated=simulator.calculateWeights()
    simulated[0]=5500
    measurement.setAxleWeight(simulated)

    Evaluator.assert_requirements(truck, measurement)
