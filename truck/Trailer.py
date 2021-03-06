import numpy as np
import json
import requests

from truck.Boogie import Boogies
class Trailer:
    """Konstruktør for Trailer-klassen
    
    Args: RegNR: Registreringsnummer for hengeren

    Funskjoner: getWeightDistribution()
    """
    # RegNR er en string
    def __init__(self, RegNR):
        
        '''
        baseLink = 'https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/kjoretoyoppslag/v1/kjennemerkeoppslag/kjoretoy/'
        URL = baseLink + RegNR
        r = requests.get(url = URL)
        data = r.json()
        '''
        data = None
        with open('truck/NP5841.txt') as lastebil:
            data = json.load(lastebil) 

        #for key in data:
            #print(data[key])


        self.lengde = data['tekniskKjoretoy']['lengde']
        self.bredde = data['tekniskKjoretoy']['bredde']
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
        self.akselInfo = []
        avstandTilNesteAksel = 0
        for aksel in range(self.antallAksler):
            self.akselInfo.append([avstandTilNesteAksel, self.aksler[aksel]['tillattLast']])
            avstandTilNesteAksel = self.aksler[aksel]['avstandtilNesteAksel']

        
        #Find Wheel boogies of Trailer
        self.boogies = Boogies(self.akselInfo)


    def getWeightDistribution(self):
        """Get weight distribution

        Ingen argumenter

        Returns: Informasjon om maks last for hver aksel som en liste
        """
        return self.akselInfo
        #for num in range(len(akselInfo)):
            #print("Avstand mellom aksel:", num+1, "og", num+2, "=", akselInfo[num][0])

        #for num in range(len(akselInfo)):
            #print("Tillatt last på aksel:", num+1,"=", akselInfo[num][1])

        return akselInfo
    def getBoogies(self):
        """
        Return all axles grouped in boogie objects after boogie type
        """
        return self.boogies


