import cv2
import tkinter as tk
from PIL import Image, ImageTk

class VideoGUI:
    def __init__(self, gui):
        self.janela = gui.janela
        self.janela.title("Tomagochi - Vídeo")
        
        self.video_label = gui.video_label
        self.video_label.pack()

        self.cap = cv2.VideoCapture('C:/Users/walla/OneDrive - Universidade Federal do Ceará/Portfólio/Tomagochi_pomodoro/Tomagochi_pomo/src/imagens/Bichinho/cat_padrao.mp4')  #% Coloque o caminho para o vídeo do seu bichinho aqui
        self.cap2 = cv2.VideoCapture('C:/Users/walla/OneDrive - Universidade Federal do Ceará/Portfólio/Tomagochi_pomodoro/Tomagochi_pomo/src/imagens/Bichinho/cat_brincar.mp4')
        self.update_video()

    def update_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            image = image.resize((300, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.video_label.configure(image=photo)
            self.video_label.image = photo # % Mantém a referência à imagem
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  #% Volta para o início do vídeo se terminar
        self.janela.after(50, self.update_video)

    def run(self):
        self.janela.mainloop()
    

import time

def barra_progresso(total, preenchido):
    largura_total = 40
    preenchido_percent = preenchido / total
    preenchido_chars = int(largura_total * preenchido_percent)
    vazio_chars = largura_total - preenchido_chars

    barra = '#' * preenchido_chars + '-' * vazio_chars

    print(f'[{barra}] {preenchido}/{total}')

# Exemplo de uso
total_progresso = 100
for i in range(total_progresso + 1):
    barra_progresso(total_progresso, i)
    time.sleep(0.1)