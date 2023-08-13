import sys
from actions import *
from pet import Pet

def main():
    status_saver = StatusSaver("status.txt") 
    load_status = status_saver.load_status()
    app = QApplication(sys.argv)
    pet = Pet(load_status)
    window = MainWindow(pet)
    window.show()

    #status_saver.save_status(pet.hunger, pet.happiness, pet.energy, pet.nivel)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()