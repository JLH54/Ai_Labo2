import sys
from Ennemies import ennemies
from PlayerClasses import playerClasses

class Mage(playerClasses):
    Mana:int

    #fireball can only target 1 person
    #Incinerate targets all ennemies
    def MageChoice(self):
        print(str(self.HealthPoints))
        print("1 : Fire ball(deals 5 damage to 1 target)")
        print("2 : Incinerate(deal 3 damage to everyone)")
        print("3 : Use your stick as a blundge weapon")
        print("3 : Protect yourself")
        print("4 : Run away like a coward")
        inGameChoice = input("")
        while(True):
            if(int(inGameChoice) != 1 and int(inGameChoice) == 2 and int(inGameChoice) == 3 and int(inGameChoice) == 4):
                print("You have to make a choice")
            else:
                return int(inGameChoice)