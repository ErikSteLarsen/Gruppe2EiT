class AdvancedSimulator:

    def __init__(self,truck):
        self.truck = truck

    def calculateWeights(self):
        # list of weight of goods on each axle
        weights = []
        axelCapacities = truck.getMaxAxleWeights()
        print("The capacity on each axle is : ")
        print(axelCapacities)
        for i in range(len[axelCapacities])
            weight = input("What is the weights of the goods on axle "+ str(i) + "?")
            weights.append(weight)
        return weights