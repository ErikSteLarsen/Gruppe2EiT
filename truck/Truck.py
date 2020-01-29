import numpy as np

import json
import requests

class Truck:

    # RegNR er en string
    def __init__(self, RegNR, Trailer):

        baseLink = 'https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/kjoretoyoppslag/v1/kjennemerkeoppslag/kjoretoy/'
        URL = baseLink + RegNR
        r = requests.get(url = URL)
        data = r.json()

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



    def getWeightDistribution(self):
        akselInfo = []
        avstandTilNesteAksel = 0
        for aksel in range(self.antallAksler):
            akselInfo.append([avstandTilNesteAksel, self.aksler[aksel]['tillattLast']])
            avstandTilNesteAksel = self.aksler[aksel]['avstandtilNesteAksel']

        if akselInfo[0][1] == None and len(akselInfo) == 3:
            akselInfo[0][1] = self.tillattTotalvekt - (akselInfo[1][1] + akselInfo[2][1])


        #for num in range(len(akselInfo)):
            #print("Avstand mellom aksel:", num+1, "og", num+2, "=", akselInfo[num][0])

        #for num in range(len(akselInfo)):
            #print("Tillatt last på aksel:", num+1,"=", akselInfo[num][1])

        return akselInfo







