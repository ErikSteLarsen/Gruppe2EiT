

class TruckMeasurement:

    '''En konstruktør for å lage et måling av en lastebil

    Args: Har ingen argumenter(Bør endres)

    Funksjoner: setAxleWeight, getTotalWeight, getMeasuredAxleWeights
    '''

    def __init__(self):
        self.measurements = [100]
        self.totalWeight = 10000  # None

    def setAxleWeight(self, measurements):
        '''Funskjon for å sette vektene fra en måling

        Args: Measurements: Liste med målinger, lengde lik antall aksler på Truck
        '''
        
        totalWeight = 0
        for weight in measurements:
            totalWeight += weight
        self.totalWeight = totalWeight
        self.measurements = measurements


    def getTotalWeight(self):
        '''Funksjon for å hente totalvekt på en måling

        Args: None

        Return: Int med totalvekt
        '''
        return self.totalWeight

    def getMeasuredAxleWeights(self):
        '''Funksjon for å hente ut akselvekten på en måling

        Args: None

        Return: Liste med akselvekter
        '''
        return self.measurements
