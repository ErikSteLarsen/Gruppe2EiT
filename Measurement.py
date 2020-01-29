

class TruckMeasurement:

    def __init__(self, Truck):
        self.truck = Truck
        self.measurements = []
        self.totalWeight = None


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


