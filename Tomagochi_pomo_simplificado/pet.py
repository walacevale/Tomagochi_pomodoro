from random import randrange
import numpy as np
class Pet:
    def __init__(self, load_status):
        
        
        self.name = 'Doutor Bicho'
        self.hunger = load_status[0]
        self.happiness = load_status[1]
        self.energy = load_status[2]
        self.nivel = load_status[3]
        self.lv_up_1 = 15
        self.lv_up_2 = 30
        self.limite_min = 0
        self.limite_max = 100
        

    def feed(self):
        casualty = randrange(0,100)
        self.hunger += 10
        self.energy -= 10
        if  casualty > 90:
            self.casualty_update()        

    def play(self):
        
        casualty = randrange(0,100)
        self.happiness += 10
        self.energy -= 30
        if  casualty > 95:
            self.casualty_update()

    def casualty_update(self):
        self.hunger -= randrange(1, 5)*10
        self.happiness -= randrange(1, 5)*10
        self.energy -= randrange(1, 5)*10

    def get_status(self):
        self.hunger = np.clip(self.hunger, self.limite_min, self.limite_max)
        self.happiness = np.clip(self.happiness, self.limite_min, self.limite_max)
        self.energy = np.clip(self.energy, self.limite_min, self.limite_max*200)
        self.nivel = np.clip(self.nivel, self.limite_min, self.limite_max)

        return  self.hunger, self.happiness, self.energy, self.nivel
    
    def born(self):
        self.name = 'Doutor Bicho'
        self.hunger = 50
        self.happiness = 50
        self.energy = 0
        self.nivel = 0

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


print(randrange(0,100))