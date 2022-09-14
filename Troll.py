import sys
from Ennemies import ennemies

class Troll(ennemies):
    HealthMultiplier:2
    WeaknessMultiplier:bool

    def isItFlame(Fire):
        if(Fire):
            WeaknessMultiplier = True
        else:
            WeaknessMultiplier = False