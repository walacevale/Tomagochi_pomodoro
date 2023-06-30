import tkinter as tk


class PetGUI:
    def __init__(self, pet, timer):
        self.pet = pet
        self.timer = timer

        self.root = tk.Tk()
        self.root.title("Tomagochi")
        self.root.geometry("400x600")

        self.video_label = tk.Label(self.root)
        self.video_label.pack()

        self.name_label = tk.Label(self.root, text=self.pet.name, font=("Arial", 16))
        self.name_label.pack()

        self.hunger_label = tk.Label(self.root, text="Nível de Fome:")
        self.hunger_label.pack()

        self.hunger_value = tk.Label(self.root, text=self.pet.hunger)
        self.hunger_value.pack()

        self.happiness_label = tk.Label(self.root, text="Humor:")
        self.happiness_label.pack()

        self.happiness_value = tk.Label(self.root, text=self.pet.happiness)
        self.happiness_value.pack()

        self.energy_label = tk.Label(self.root, text="Energia:")
        self.energy_label.pack()

        self.energy_value = tk.Label(self.root, text=self.pet.energy)
        self.energy_value.pack()

        self.feed_button = tk.Button(self.root, text="Alimentar", command=self.feed_pet)
        self.feed_button.pack()

        self.play_button = tk.Button(self.root, text="Brincar", command=self.play_with_pet)
        self.play_button.pack()

        self.clock_label = tk.Label(self.root, text="00:00", font=("Arial", 16))
        self.clock_label.pack()

        self.start_button = tk.Button(self.root, text="Iniciar", command=self.timer.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Parar", command=self.timer.stop_timer)
        self.stop_button.pack()

        born_button = tk.Button(self.root, text="Nascer", command=self.play_born)
        born_button.place(x=2, y=10)

        self.timer_running = False
        self.start_time = None

    def feed_pet(self):
        self.pet.feed()
        self.update_status()

    def play_with_pet(self):
        self.pet.play()
        self.update_status()

    def play_born(self):
        self.pet.born()
        self.update_status()

    def update_status(self):
        hunger, happiness, energy = self.pet.get_status()
        self.hunger_value.config(text=hunger)
        self.happiness_value.config(text=happiness)
        self.energy_value.config(text=energy)

 

    def run(self):
        self.root.mainloop()
