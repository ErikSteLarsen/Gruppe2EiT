import numpy as np

import requests

class Lastebil:

    # RegNR er en string
    def __init__(self, RegNR):

        baseLink = 'https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/kjoretoyoppslag/v1/kjennemerkeoppslag/kjoretoy/'
        URL = baseLink + RegNR
        r = requests.get(url = URL)
        data = r.json()
        for key in data:
            print(key, data[key])
            #print(data)

        self.lengde = data['tekniskKjoretoy']['lengde']
        self.bredde = data['tekniskKjoretoy']['bredde']
        self.hoyde = data['tekniskKjoretoy']['hoyde']
        self.egenvekt = data['tekniskKjoretoy']['lastegenskaper']['egenvekt']
        self.tillattTotalvekt = data['tekniskKjoretoy']['lastegenskaper']['tillattTotalvekt']
        self.nyttelast = data['tekniskKjoretoy']['lastegenskaper']['nyttelast']
        self.tillattVogntogvekt = data['tekniskKjoretoy']['lastegenskaper']['tillattVogntogvekt']
        self.tillattTilhengervektMedBrems = data['tekniskKjoretoy']['lastegenskaper']['tillattTilhengervektMedBrems']
        self.tillattTilhengervektUtenBrems = data['tekniskKjoretoy']['lastegenskaper']['tillattTilhengervektUtenBrems']


        self.antallAksler = len(data['tekniskKjoretoy']['aksler']['aksler'])
        print(self.antallAksler)
        # Aksler
        print(data['tekniskKjoretoy']['aksler']['aksler'])



        print("lengde:", self.lengde)
