class Pet:
    def __init__(self, load_status):
        self.name = 'Doutor Bicho'
        self.hunger = load_status[0]
        self.happiness = load_status[1]
        self.energy = load_status[2]

    def feed(self):
        self.hunger += 30
        self.energy -= 20

    def play(self):
        self.happiness += 20
        self.energy -= 30

    def update(self):
        self.hunger += 1
        self.happiness -= 1
        self.energy -= 1

    def get_status(self):
        return self.hunger, self.happiness, self.energy
    
    def born(self):
        self.name = 'Doutor Bicho'
        self.hunger = 100
        self.happiness = 100
        self.energy = 0
        
    

class StatusSaver:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_status(self, hunger, happiness, energy):
        status_text = f"Nivel de Fome: {hunger}\n Humor: {happiness}\n Energia: {energy} \n"

        with open(self.file_path, "w") as file:
            file.write(status_text)

    def load_status(self):
        try:
            with open(self.file_path, "r") as file:
                status_lines = file.readlines()

            hunger = int(status_lines[0].split(": ")[1])
            happiness = int(status_lines[1].split(": ")[1])
            energy = int(status_lines[2].split(": ")[1])

            return hunger, happiness, energy

        except FileNotFoundError:
            return None

        except (IndexError, ValueError):
            print("Erro ao carregar o arquivo de status.")
            return None