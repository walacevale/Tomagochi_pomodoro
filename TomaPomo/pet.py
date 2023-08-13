from random import randrange
import numpy as np

class Pet:
    def __init__(self, load_status):
        
        
        self.name = 'Doutor Bicho'
        self.hunger = load_status[0]
        self.happiness = load_status[1]
        self.energy = load_status[2]
        self.nivel = load_status[3]

    def play(self):
        self.happiness += 10
    
    def feed(self):
        self.hunger += 10

    def increment_nivel(self):
        self.nivel += 1
        print(f"Nível incrementado para: {self.nivel}")

    def get_status(self):
        return self.hunger, self.happiness, self.nivel
    

class StatusSaver:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_status(self, hunger, happiness, energy, nivel):
        status_text = f"Nivel de Fome: {hunger}\n Humor: {happiness}\n Energia: {energy} \n Nivel: {nivel}"

        with open(self.file_path, "w") as file:
            file.write(status_text)

    def load_status(self):
        try:
            with open(self.file_path, "r") as file:
                status_lines = file.readlines()

            hunger = int(status_lines[0].split(": ")[1])
            happiness = int(status_lines[1].split(": ")[1])
            energy = int(status_lines[2].split(": ")[1])
            nivel = int(status_lines[3].split(": ")[1])
            
            return hunger, happiness, energy, nivel

        except FileNotFoundError:
            return None

        except (IndexError, ValueError):
            print("Erro ao carregar o arquivo de status.")
            return None