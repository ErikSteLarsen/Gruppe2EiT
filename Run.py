#from truck.Truck import Truck
from truck.Truck import Truck
from Measurement import TruckMeasurement
from evaluator.evaluator import Evaluator

lastebil = "DP51062"
henger = "NP5841"

if __name__ == '__main__':
    truck = Truck(lastebil, henger)
    print(truck.getMaxAxelWeights())
    print(truck.trailer.getWeightDistribution())

    measurement = TruckMeasurement(truck)
    measurement.setAxleWeight([5000, 7544, 2344, 2343])

    Evaluator.assert_requirements(truck, measurement)
