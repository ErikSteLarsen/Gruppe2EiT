"""
This file include the Truck object and its functions for extracting information from NPRA (Norwegian Public Road Administration). Its constructor require a Truck license plate number and might also use a trailer license plate.
"""


import numpy as np

import json
import requests

from truck.Trailer import Trailer
from truck.Boogie import Boogies
class Truck:
    """Konstruktør for Truck-klassen(Lastebil)

    Args: 
    RegNR: Registreringsnummer for lastebil\t
    trailerRegNR: Registreringsnummer for tilhenger, ikke nødvendig hvis det ikke er henger

    Funskjoner: getMaxAxelWeights(), getNumberOfAxles(), getMaxTruckTotalWeight(), getTillattVogntogVekt()
    """
    # RegNR er en string
    def __init__(self, RegNR, trailerRegNR=None):

        """
        Initialization of Truck object. 
        Input: Norwegian license plate numbers
        Return: Truck object with vales from NPRA
        """
        baseLink = 'https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/kjoretoyoppslag/v1/kjennemerkeoppslag/kjoretoy/'
        URL = baseLink + RegNR
        r = requests.get(url = URL)
        data = r.json()
        '''

        data = None
        with open('truck/DP51062.txt') as lastebil:
            data = json.load(lastebil)  
        '''

        #for key in data:
            #print(data[key])

        self.lengde = data['tekniskKjoretoy']['lengde']
        self.bredde = data['tekniskKjoretoy']['bredde']
        self.hoyde = data['tekniskKjoretoy']['hoyde']
        self.egenvekt = data['tekniskKjoretoy']['lastegenskaper']['egenvekt']
        self.tillattTotalvekt = data['tekniskKjoretoy']['lastegenskaper']['tillattTotalvekt']
        self.nyttelast = data['tekniskKjoretoy']['lastegenskaper']['nyttelast']
        self.tillattVogntogvekt = data['tekniskKjoretoy']['lastegenskaper']['tillattVogntogvekt']
        self.tillattTilhengervektMedBrems = data['tekniskKjoretoy']['lastegenskaper']['tillattTilhengervektMedBrems']
        self.tillattTilhengervektUtenBrems = data['tekniskKjoretoy']['lastegenskaper']['tillattTilhengervektUtenBrems']

        # Antall aksler
        self.antallAksler = len(data['tekniskKjoretoy']['aksler']['aksler'])

        # Denne returnerer et array med en dictionary per aksel, gå inn via "self.aksler[nummer].avstandtilNesteAksel" feks
        self.aksler = data['tekniskKjoretoy']['aksler']['aksler']
        if trailerRegNR is None:
            self.trailer=None
        else:
            self.trailer = Trailer(trailerRegNR)



        self.akselInfo = []

        avstandTilNesteAksel = 0

        for aksel in range(self.antallAksler):
            self.akselInfo.append([avstandTilNesteAksel, self.aksler[aksel]['tillattLast']])
            avstandTilNesteAksel = self.aksler[aksel]['avstandtilNesteAksel']

        if self.akselInfo[0][1] == None and len(self.akselInfo) == 3:
            self.akselInfo[0][1] = self.tillattTotalvekt - (self.akselInfo[1][1] + self.akselInfo[2][1])
        
        """
        Find wheel boogies of 
        """
        self.boogies = Boogies(self.akselInfo)
        #for num in range(len(akselInfo)):
            #print("Avstand mellom aksel:", num+1, "og", num+2, "=", akselInfo[num][0])

        #for num in range(len(akselInfo)):
            #print("Tillatt last på aksel:", num+1,"=", akselInfo[num][1])

    def getMaxAxleWeights(self):
        """
        Return maximum allowed axle weights for the truck as an array. Index 0 is first axle in front of veichle
        """
        return self.akselInfo

    def getNumberOfAxles(self):
        """
        Return the trucks number of axles
        """
        return self.antallAksler


    def getMaxTruckTotalWeight(self):
        """
        Return max total weight of truck. 
        Remark: not including trailer
        """
        return self.tillattTotalvekt

    def getMaxTruckAndTrailerTotalWeight(self):
        """
        Return max total weight of truck and trailer based on trucks info
        """

        return self.tillattVogntogvekt

    def getBoogies(self):
        """
        Return all axles grouped in boogie objects after boogie type
        """
        return self.boogies

