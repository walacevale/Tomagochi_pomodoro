from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSpinBox
from PyQt5.QtCore import QTimer, Qt, pyqtSignal


class Cronometro(QWidget):
    time_finished = pyqtSignal()

    def __init__(self, pet_instance):
        super().__init__()
        self.pet =  pet_instance
        
        layout = QVBoxLayout(self)


        # Elementos do Cronômetro
        self.timer_spinbox = QSpinBox()
        self.timer_spinbox.setMaximum(60)  # Máximo de 60 minutos
        self.timer_spinbox.setMinimum(1)  # Mínimo de 1 minuto
        self.timer_spinbox.setFixedSize(50, 25)
        self.timer_spinbox.setStyleSheet("font-size: 24px;")
        layout.addWidget(self.timer_spinbox)
        layout.setAlignment(self.timer_spinbox, Qt.AlignHCenter)



        self.timer_display = QLabel("Escolha o tempo do seu Pomodoro!!")
        self.timer_display.setStyleSheet("font-size: 16px;")
        self.timer_display.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.timer_display)

        self.start_btn = QPushButton("Iniciar")
        self.start_btn.clicked.connect(self.start_timer)
        self.start_btn.setFixedSize(100, 50)       
        self.start_btn.setStyleSheet("""
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            border-radius: 4px;
        }

        QPushButton:hover {
            background-color: #45a049;
        }
        """)
        layout.addWidget(self.start_btn)
        layout.setAlignment(self.start_btn, Qt.AlignHCenter)

        self.reset_btn = QPushButton("Resetar")
        self.reset_btn.clicked.connect(self.reset_timer)
        self.reset_btn.setFixedSize(100, 50)       
        self.reset_btn.setStyleSheet("""
        QPushButton {
            background-color: #FF0000;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            border-radius: 4px;
        }

        QPushButton:hover {
            background-color: #E60000;
        }
        """)
        layout.addWidget(self.reset_btn)
        layout.setAlignment(self.reset_btn, Qt.AlignHCenter)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.time_left = 0

        self.setLayout(layout)

    def start_timer(self):
        if not self.timer.isActive():
            self.time_left = self.timer_spinbox.value() * 60  # Converta para segundos
            self.timer.start(1000)  # atualizar a cada segundo

    def reset_timer(self):
        self.timer.stop()
        self.time_left = 0
        self.timer_display.setText("Escolha o tempo do seu Pomodoro!!")

    def update_timer(self):
        
        if self.time_left > 0:
            self.time_left -= 1
            mins, secs = divmod(self.time_left, 60)
            self.timer_display.setText(f"{mins:02}:{secs:02}")
          
            

        else:
            print("Tempo esgotado!")
            self.timer.stop()
            self.pet.increment_nivel()
            self.time_finished.emit()


            # Você pode adicionar alguma ação a ser tomada quando o tempo acabar
