from truck.Truck import Truck

lastebil = "DP51062"
henger = "NP5841"

if __name__ == '__main__':
    truck = Truck(lastebil,henger)
    print(truck.getMaxAxelWeights())
    print(truck.trailer.getWeightDistribution())
