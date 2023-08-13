from random import randrange
import numpy as np

class Pet:
    def __init__(self):
        
        
        self.name = 'Doutor Bicho'
        self.nivel = 0
        self.hunger = 10
        self.happiness = 10
        self.energy = 100

    def play(self):
        self.happiness += 10
    
    def feed(self):
        self.hunger += 10

    def increment_nivel(self):
        self.nivel += 1
        print(f"Nível incrementado para: {self.nivel}")

    def get_status(self):
        return self.hunger, self.happiness, self.nivel