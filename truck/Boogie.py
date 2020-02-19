"""
This file include the boogie object used to store boogies within the truck and trailer objects. 
"""

import numpy as np

class Boogie:
    """
    Args:
    Wheelset from Truck or Trailer object

    """
    def __init__(self, boogieWheels, axleDistance = None, driveShaft = False):
        self.axleDistance = axleDistance
        self.boogieWheels = boogieWheels
        self.driveShaft = driveShaft

class Boogies:
    """
    Creates an array of all wheelsets on a Truck or Trailer object
    INIT: list of Axles with maxWeight and distance to next axle
    
    Wheelset can be extracted with getBoogies()
    """
    def __init__(self, axles):
        self.boogies = [] #List of Boogie objects
        for i in range(1, len(axles)):
            if(axles[i][0] < 1800):
                if(i >= len(axles)-1): #if last axle
                    self.boogies.append(Boogie([i-1, i], axles[i][0]))
                elif(axles[i+1][0] < 1800):
                    self.boogies.append(Boogie([i-1, i, i+1], min(axles[i-1][0], axles[i][0])))
                    i = i+2
                else:
                    self.boogies.append(Boogie([i-1, i], axles[i][0]))
                    i = i+1
            else:
                self.boogies.append(Boogie([i-1]))

    def getBoogies(self):
        return self.boogies
