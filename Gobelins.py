import sys
from Ennemies import ennemies

class Gobelins(ennemies): 
    Weapon:str
    HasShield:bool
    ShieldPoints:int

    def Shielded(HasShield):
        if HasShield:
            ShieldPoints = 5 * difficulty
        else:
            ShieldPoints = 0
    
    def WeaponEquipped():
        match difficulty:
            case 1:
                AttackPoint = 5
                return Weapon == "Stick"
            case 2:
                AttackPoint = 8
                return Weapon == "Knife"
            case 3:
                AttackPoint = 13
                return Weapon == "Sword"
            case _:
                return "Something is wrong with the gobelin"