import tkinter as tk
from draw import ASCIIImages
from pet import Pet
from timer import Cronometro


class Action:

    def __init__(self, pet):

        self.janela = tk.Tk()
        self.pet = pet
        self.ASCIIImages = ASCIIImages
        self.Cronometro = Cronometro

        self.janela.title("Tomagochi")
        self.janela.geometry("400x350")
        self.caixa_texto = tk.Text(self.janela, width=25, height=16, state='disabled')
        self.caixa_texto.grid(row=0, column=0, padx=10, pady=10)      
        self.exibir_intro()

        self.name_label = tk.Label(self.janela, text=self.pet.name, font=("Arial", 16))
        self.name_label.place(x=220, y=10)

        self.hunger_label = tk.Label(self.janela, text="Hunger:")
        self.hunger_label.place(x=220, y=50)

        self.hunger_value = tk.Label(self.janela, text=self.pet.hunger)
        self.hunger_value.place(x=265, y=50)

        self.happiness_label = tk.Label(self.janela, text="Humor:")
        self.happiness_label.place(x=220, y=70)

        self.happiness_value = tk.Label(self.janela, text=self.pet.happiness)
        self.happiness_value.place(x=265, y=70)

        self.energy_label = tk.Label(self.janela, text="Energia:")
        self.energy_label.place(x=220, y=90)

        self.energy_value = tk.Label(self.janela, text=self.pet.energy)
        self.energy_value.place(x=265, y=90)

        self.nivel_label = tk.Label(self.janela, text="Nivel:")
        self.nivel_label.place(x=220, y=110)

        self.nivel_label = tk.Label(self.janela, text=self.pet.nivel)
        self.nivel_label.place(x=265, y=110)

        self.feed_button = tk.Button(self.janela, text="Alimentar", command=self.feed_pet)
        self.feed_button.place(relx=0.2, rely=0.9, anchor=tk.CENTER,  width=80, height=50)

        self.play_button = tk.Button(self.janela, text="Brincar", command=self.play_with_pet)
        self.play_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER,  width=80, height=50)

        self.examiner_button = tk.Button(self.janela, text="Cat examiner", command=self.cat_examiner)
        self.examiner_button.place(relx=0.8, rely=0.6, anchor=tk.CENTER,  width=80, height=50)



    def write_text(self, text):
            self.caixa_texto.config(state='normal')
            self.caixa_texto.insert(tk.END, text)
            self.caixa_texto.insert(tk.END, "\n")
            self.caixa_texto.config(state='disabled')
            self.caixa_texto.see(tk.END)
    
    def feed_pet(self):
        if self.pet.energy > 30:
            self.feed_button.config(state=tk.NORMAL)
            self.pet.feed()
            self.write_text('Your pet has been fed!!')
            self.update_status()
            if self.pet.hunger >= 80  and self.pet.happiness >= 80:
                self.pet.nivel += 1
                self.update_status()          
            if self.pet.nivel <= self.pet.lv_up_1:
                self.write_text(ASCIIImages.ovo())
            if self.pet.nivel > self.pet.lv_up_1:
                self.write_text(ASCIIImages.gato_alimentar())
            
        else:
            self.feed_button.config(state=tk.DISABLED)

    def play_with_pet(self):
        if self.pet.energy > 0:
            self.play_button.config(state=tk.NORMAL)
            self.pet.play()
            self.write_text('"You played with your cat!!')
            self.update_status()
            if self.pet.hunger >= 80  and self.pet.happiness >= 80:
                self.pet.nivel += 1
                self.update_status()
            if self.pet.nivel <= self.pet.lv_up_1:
                self.write_text(ASCIIImages.ovo())
            if self.pet.nivel > self.pet.lv_up_1:
                self.write_text(ASCIIImages.gato_brincando())
            self.evolution()
        else:
            self.play_button.config(state=tk.DISABLED)

    def play_born(self):
        self.pet.born()
        self.update_status()
        

    def update_status(self):
        hunger, happiness, energy, nivel = self.pet.get_status()
        self.hunger_value.config(text=hunger)
        self.happiness_value.config(text=happiness)
        self.energy_value.config(text=energy)
        self.nivel_label.config(text=nivel)

    def exibir_intro(self):
        self.caixa_texto.config(state='normal')
        self.caixa_texto.insert(tk.END, self.ASCIIImages.intro())
        self.caixa_texto.insert(tk.END, "\n")
        self.caixa_texto.config(state='disabled')
        self.caixa_texto.see(tk.END)

    def evolution(self):
        if self.pet.nivel == self.pet.lv_up_1:
            self.write_text(ASCIIImages.lv_up()) 
        if self.pet.nivel == self.pet.lv_up_2:
            self.write_text(ASCIIImages.lv_up()) 

    def cat_examiner(self):
        if self.pet.nivel <= self.pet.lv_up_1:
            self.write_text(ASCIIImages.ovo()) 
        if self.pet.nivel > self.pet.lv_up_1:
            self.write_text(ASCIIImages.gato_lv1())
        if self.pet.nivel > self.pet.lv_up_2:
            self.write_text(ASCIIImages.gato_lv2())
        if self.pet.hunger < 40:
            self.write_text('Your cat looks hungry.')
        if self.pet.happiness < 40:
            self.write_text('Your cat looks sad.')
        if self.pet.happiness > 40 and self.pet.hunger > 40:
            self.write_text('Your cat looks happy and healthy.')        