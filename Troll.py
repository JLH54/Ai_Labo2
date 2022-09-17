import sys
from Ennemies import ennemies
import random

class Troll(ennemies):
    HealthMultiplier:2
    WeaknessMultiplier:bool

    def behaviour(self, player):
        self.protected = False
        actionDecider = random.randrange(0,101)
        if(self.dead == False):
            if(actionDecider >= 0 and actionDecider <= 40):
                self.goblinAttack(player)
            elif(actionDecider >= 41 and actionDecider <= 80):
                self.goblinProtect()
            elif(actionDecider >= 81 and actionDecider <= 100):
                print(self.CarachterName + " is laughing at you")
    
    def __init__(self, name, level):
        super().__init__(name, level)
        self.HealthPoints = 20
        self.AttackPoint = random.randrange(8,12) * level
        self.className = "Troll"