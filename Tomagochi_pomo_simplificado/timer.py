import tkinter as tk
import time
from pet import Pet


class Cronometro:

    def __init__(self,pet, action):
        self.janela = tk.Tk()
        self.pet = pet
        self.action = action
        self.janela.title("Cronômetro")
        self.janela.geometry("200x100")
         

        self.label_tempo = tk.Label(self.janela, text="00:00", font=("Arial", 24))
        self.label_tempo.pack(pady=10)

        self.botao_iniciar = tk.Button(self.janela, text="Iniciar", command=self.iniciar_cronometro)
        self.botao_iniciar.pack(side=tk.LEFT, padx=10)

        self.botao_parar = tk.Button(self.janela, text="Parar", command=self.parar_cronometro)
        self.botao_parar.pack(side=tk.LEFT, padx=10)

        self.botao_resetar = tk.Button(self.janela, text="Resetar", command=self.resetar_cronometro)
        self.botao_resetar.pack(side=tk.LEFT, padx=10)

        self.tempo_inicial = 0
        self.tempo_parado = 0
        self.cronometro_funcionando = False

    def iniciar_cronometro(self):
        if not self.cronometro_funcionando:
            self.tempo_inicial = time.time() - self.tempo_parado
            self.cronometro_funcionando = True
            self.atualizar_cronometro()

    def parar_cronometro(self):
        if self.cronometro_funcionando:
            self.tempo_parado = time.time() - time.time() 
            self.cronometro_funcionando = False

    def atualizar_cronometro(self):
        if self.cronometro_funcionando:
            tempo_atual = time.time() - self.tempo_inicial
            tempo_formatado = self.formatar_tempo(tempo_atual)
            self.label_tempo.configure(text=tempo_formatado)
            self.janela.after(1000, self.atualizar_cronometro)

            if int(tempo_atual) == 3:
                self.pet.energy += 50
                self.action.update_status()
                

    def resetar_cronometro(self):
        self.tempo_inicial = time.time()
        self.tempo_parado = 0
        self.cronometro_funcionando = False
        self.label_tempo.configure(text="00:00")

    def formatar_tempo(self, tempo):
        segundos = int(tempo % 60)
        minutos = int((tempo // 60) % 60)
        
        return f"{minutos:02d}:{segundos:02d}"
    
    def iniciar_interface(self):
        self.janela.mainloop()



