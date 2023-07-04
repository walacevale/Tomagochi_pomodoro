import tkinter as tk
from draw import ASCIIImages
from pet import Pet


class Action:

    def __init__(self, pet):

        self.janela = tk.Tk()
        self.pet = pet
        self.ASCIIImages = ASCIIImages
        self.janela.title("Tomagochi")
        self.janela.geometry("400x600")
        self.caixa_texto = tk.Text(self.janela, width=25, height=16, state='disabled')
        self.exibir_intro()
        self.caixa_texto.pack()        
        

        self.name_label = tk.Label(self.janela, text=self.pet.name, font=("Arial", 16))
        self.name_label.pack()

        self.hunger_label = tk.Label(self.janela, text="Nível de Fome:")
        self.hunger_label.pack()

        self.hunger_value = tk.Label(self.janela, text=self.pet.hunger)
        self.hunger_value.pack()

        self.happiness_label = tk.Label(self.janela, text="Humor:")
        self.happiness_label.pack()

        self.happiness_value = tk.Label(self.janela, text=self.pet.happiness)
        self.happiness_value.pack()

        self.energy_label = tk.Label(self.janela, text="Energia:")
        self.energy_label.pack()

        self.energy_value = tk.Label(self.janela, text=self.pet.energy)
        self.energy_value.pack()

        self.feed_button = tk.Button(self.janela, text="Alimentar", command=self.feed_pet)
        self.feed_button.pack()

        self.play_button = tk.Button(self.janela, text="Brincar", command=self.play_with_pet)
        self.play_button.pack()

    
    def feed_pet(self):
        self.pet.feed()
        self.update_status()
        self.update_status()
        self.caixa_texto.config(state='normal')
        self.caixa_texto.insert(tk.END, self.ASCIIImages.gato_alimentar())
        self.caixa_texto.insert(tk.END, "\n")
        self.caixa_texto.config(state='disabled')
        self.caixa_texto.see(tk.END)


    def play_with_pet(self):
        self.pet.play()
        self.update_status()
        self.caixa_texto.config(state='normal')
        self.caixa_texto.insert(tk.END, self.ASCIIImages.gato_brincando())
        self.caixa_texto.insert(tk.END, "\n")
        self.caixa_texto.config(state='disabled')
        self.caixa_texto.see(tk.END)


    def play_born(self):
        self.pet.born()
        self.update_status()
        

    def update_status(self):
        hunger, happiness, energy = self.pet.get_status()
        self.hunger_value.config(text=hunger)
        self.happiness_value.config(text=happiness)
        self.energy_value.config(text=energy)

 
    
    def exibir_ok(self):
        self.caixa_texto.config(state='normal')
        self.caixa_texto.insert(tk.END, self.ASCIIImages.ovo())
        self.caixa_texto.insert(tk.END, "\n")
        self.caixa_texto.config(state='disabled')
        self.caixa_texto.see(tk.END)

    def exibir_okk(self):
        self.caixa_texto.config(state='normal')
        self.caixa_texto.insert(tk.END, self.ASCIIImages.gato_lv2())
        self.caixa_texto.insert(tk.END, "\n")
        self.caixa_texto.config(state='disabled')
        self.caixa_texto.see(tk.END)

    def exibir_intro(self):
        self.caixa_texto.config(state='normal')
        self.caixa_texto.insert(tk.END, self.ASCIIImages.intro())
        self.caixa_texto.insert(tk.END, "\n")
        self.caixa_texto.config(state='disabled')
        self.caixa_texto.see(tk.END)

    def update_status(self):
        hunger, happiness, energy = self.pet.get_status()
        self.hunger_value.config(text=hunger)
        self.happiness_value.config(text=happiness)
        self.energy_value.config(text=energy)

    #----buttons---#
