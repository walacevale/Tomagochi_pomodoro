from random import randrange
import numpy as np

class Pet:
    def __init__(self):
        
        
        self.name = 'Doutor Bicho'
        self.hunger = 10
        self.happiness = 10
        self.energy = 100

    def play(self):
        self.happiness += 10
    
    def feed(self):
        self.hunger += 10

    def get_status(self):
        return self.hunger, self.happiness