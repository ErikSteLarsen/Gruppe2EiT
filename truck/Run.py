from Truck import Truck
from Trailer import Trailer

lastebil = "DP51062"
henger = "NP5841"

if __name__ == '__main__':
    truck = Truck(lastebil,henger)
    print(truck.getWeightDistribution())
    print(truck.trailer.getWeightDistribution())
