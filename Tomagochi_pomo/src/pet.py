class Pet:
    def __init__(self):
        self.name = 'Doutor bicho'
        self.hunger = 100
        self.happiness = 100
        self.energy = 0

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
