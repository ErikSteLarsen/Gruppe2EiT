

class TruckMeasurement:

    def __init__(self):
        self.measurements = [100]
        self.totalWeight = 10000 #None


    def setAxleWeight(self, measurements):
        totalWeight = 0
        for weight in measurements:
            totalWeight += weight
        self.totalWeight = totalWeight
        self.measurements = measurements


    def getTotalWeight(self):
        return self.totalWeight


    def getMeasuredAxleWeights(self):
        return self.measurements


