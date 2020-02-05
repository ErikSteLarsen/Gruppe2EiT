class Simulator:

    def __init__(self,truck):
        self.truck = truck

    def calculateWeights(self):
        numAxles=self.truck.getNumberOfAxles()
        if self.truck.trailer is not None:
            numAxles+=+self.truck.trailer.antallAksler
        weights=[4000]*numAxles
        return weights
