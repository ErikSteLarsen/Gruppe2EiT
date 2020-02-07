class Simulator:
    '''
    Konstruktør for simulator klassen

    Args: truck: Tar inn et truckobjekt 
    '''
    def __init__(self,truck):
        self.truck = truck

    def calculateWeights(self):
        '''
        Enkel vektsimulator som returnerer en liste med vekter for hver aksel på lastebilen

        Args: Ingen argumenter
        '''
        numAxles=self.truck.getNumberOfAxles()
        if self.truck.trailer is not None:
            numAxles+=+self.truck.trailer.antallAksler
        weights=[4000]*numAxles
        return weights
