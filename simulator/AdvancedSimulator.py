import numpy as np


class AdvancedSimulator:

    def __init__(self,truck):
        self.truck = truck

    def calculateWeights(self):

        weights = []
        axleCapacitiesTruck = self.truck.getMaxAxleWeights()
        axleCapacitiesTrailer = self.truck.trailer.getWeightDistribution()
        allCapacities = axleCapacitiesTruck
        for element in axleCapacitiesTrailer:
            allCapacities.append(element)

        print(allCapacities)
        print("The capacity on each axle is : ")
        # TODO Legg til at dette kan sjekkes på henger også
        print("Truck:", axleCapacitiesTruck, "\nTrailer:", axleCapacitiesTrailer)

        for i in range(len(allCapacities)):
            weight = int(input("What is the weights of the goods on axle "+ str(i) + "?"))
            weights.append(weight)

        return weights
