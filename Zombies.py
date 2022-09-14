import sys
from Ennemies import ennemies

class Zombies(ennemies):
    HordeMultiplier:bool
    DamageDeMultiplier:int
    AttackPoint = 6
    HealthPoints = 10
    MaxHealthPoints = HealthPoints

    def IsItInAHorde(numbersOfZombiesAround):
        if(numbersOfZombiesAround >= 3):
            HordeMultiplier = True
        else:
            HordeMultiplier = False

    def Decapitated():
        AttackPoint = AttackPoint - ((MaxHealthPoints - HealthPoints  / 2))