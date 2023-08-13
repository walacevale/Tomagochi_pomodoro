from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QProgressBar
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer
from pet import *
from cronometro import Cronometro



class MainWindow(QWidget):
    def __init__(self,pet):
        super(MainWindow, self).__init__()
        layout = QVBoxLayout()
        self.pet = pet()

        self.movie_screen = QLabel()
        self.movie = QMovie("normal.gif")
        self.movie_screen.setMovie(self.movie)
        layout.addWidget(self.movie_screen)

        # Inicia com a animação padrão
        self.movie.stop()
        self.movie = QMovie("./TomaPomo\image\padrao.gif")
        self.movie_screen.setMovie(self.movie)
        self.movie.start()

        self.btn_brincar = QPushButton("Brincar")
        self.btn_brincar.clicked.connect(self.brincar)
        layout.addWidget(self.btn_brincar)

        self.btn_alimentar = QPushButton("Alimentar")
        self.btn_alimentar.clicked.connect(self.alimentar)
        layout.addWidget(self.btn_alimentar)

        self.fome_bar = QProgressBar(self)
        self.fome_bar.setFixedSize(200, 30)
        self.fome_bar.setAlignment(Qt.AlignCenter)
        self.fome_bar.setValue(self.pet.hunger)  # Converta para porcentagem
        self.setStyle(self.fome_bar)        
        layout.addWidget(self.fome_bar)

        self.happiness_bar = QProgressBar(self)
        self.happiness_bar.setAlignment(Qt.AlignCenter)
        self.happiness_bar.setValue(self.pet.happiness)  # Converta para porcentagem
        self.setStyle(self.happiness_bar)
        layout.addWidget(self.happiness_bar)

        self.cronometro = Cronometro(self.pet) #cronometro
        self.cronometro.time_finished.connect(self.update_level)
        layout.addWidget(self.cronometro)

        self.level_label = QLabel(f'Nível: {self.pet.nivel}')
        layout.addWidget(self.level_label)

        self.setLayout(layout)
        
    def brincar(self):
        self.pet.play()
        self.update_status()
        self.movie.stop()
        self.movie = QMovie("./TomaPomo\image/brincando.gif")
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        QTimer.singleShot(8000, self.resetar) # brincar por 5 segundos

    def alimentar(self):
        self.pet.feed()
        self.update_status()
        self.movie.stop()
        self.movie = QMovie("./TomaPomo\image\comendo.gif")
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        QTimer.singleShot(8000, self.resetar) # alimentar por 5 segundos


    def resetar(self):
        self.movie.stop()
        self.movie = QMovie("./TomaPomo\image\padrao.gif")
        self.movie_screen.setMovie(self.movie)
        self.movie.start()

    def update_status(self):
        self.fome_bar.setValue(self.pet.hunger)
        self.happiness_bar.setValue(self.pet.happiness)


    def update_level(self):
        print(f"Atualizando nível para: {self.pet.nivel}")
        self.level_label.setText(f'Nível: {self.pet.nivel}')      
        

    def setStyle(self, bar):
        bar.setStyleSheet("QProgressBar"
                          "{"
                            "background-color :  rgba(255, 0, 0, 255);"
                            "border : 1px"
                          "}"
  
                          "QProgressBar::chunk"
                          "{"
                            "background : rgba(0, 255, 0, 200);"
                          "}"
                          )
