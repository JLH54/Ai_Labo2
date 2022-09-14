import sys
from Actor import actor

class ennemies(actor):
    def __init__(self, name, level):
        super().__init__(name)
        self.difficulty = level
    difficulty:int