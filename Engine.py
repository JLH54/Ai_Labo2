from pickle import TRUE
from random import random
import sys
from PlayerClasses import playerClasses
from Rogue import Rogue
#from Knight import Knight
from Mage import Mage
from Gobelins import Gobelins
from Troll import Troll
from Zombies import Zombies

class engine():
    global ForestTaken
    global SwampTaken
    global CaveTaken
    global player
    def GameStarted(self):
        inGame = 1
        while(inGame == 1):
            print("Welcome to my rpg!")
            print("1 : start game")
            print("2 : close game")
            inGameChoice = input("")
            if (int(inGameChoice) == 1):
                return 1
            elif (int(inGameChoice) != 1):
                return 0  

    def PlayerChoice(self):
        print("What is your name?")
        Player_Name = input("")
        print("Choose your class:\n")
        print("1 : Knight\n")
        print("2 : Mage\n")
        print("3 : Rogue\n")
        inGameChoice = input("") 
        if (int(inGameChoice) == 1):
            #player = Knight()
            player = Mage(Player_Name, inGameChoice)
            return player
        elif (int(inGameChoice) == 2):
            player = Mage(Player_Name, inGameChoice)
            return player
        elif(int(inGameChoice) == 3):
            player = Rogue(Player_Name, inGameChoice)
            return player
        elif(int(inGameChoice) != 1 or int(inGameChoice) != 2 or int(inGameChoice) != 3):
            print("You have made no choice")
            inGameChoice = self.PlayerChoice()

    def PlayerChooseThePlace(self):
        global ForestTaken
        global SwampTaken
        global CaveTaken
        ForestTaken = False
        SwampTaken = False
        CaveTaken = False
        print("The king needs you to clean those places")
        while(True):
            if(ForestTaken == False):
                print("1 : forest of goblins")
            if(SwampTaken == False):
                print("2 : swamp of zombies")
            if(CaveTaken == False):
                print("3 : cave of trolls")
            inGameChoice = input("")
            if(int(inGameChoice) ==1):
                if(ForestTaken == True):
                    print("You have already been there it's clean")
                else:
                    ForestTaken = True
                    return 1
            if(int(inGameChoice) ==2):
                if(SwampTaken == True):
                    print("You have already been there it's clean")
                else:
                    SwampTaken = True
                    return 2
            if(int(inGameChoice) == 3):
                if(CaveTaken == True):
                    print("You have already been there it's clean")
                else:
                    CaveTaken = True
                    return 3

    def PlaceChosen(self):
        place_chosen = self.PlayerChooseThePlace()
        if(place_chosen == 1):
            how_many_goblins = random.randrange(2,3)
            goblins = []
            for i in how_many_goblins:
                goblin = Gobelins()
                goblins.append(goblin)
        if(place_chosen == 2):
            how_many_zombies = random.randrange(1,5)
            zombies = []
            for i in how_many_zombies:
                zombie = Zombies()
                zombies.append(zombie)
        if(place_chosen == 3):
            how_many_trolls = random.randrange(1,2)
            trolls = []
            for i in how_many_trolls:
                troll = Troll()
                trolls.append(troll)

    def PlayerTurn(self):
        

    def start(self):
        started = self.GameStarted()
        while(started == 1):
            player = self.PlayerChoice()
            self.PlaceChosen()
            started = 0

    def __init__(self):
        ForestTaken = False
        SwampTaken = False
        CaveTaken = False
        self.start()