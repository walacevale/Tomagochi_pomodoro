from pet import Pet, StatusSaver
from gui import PetGUI
from timer import Timer
from video_gui import VideoGUI


def main():
    
    status_saver = StatusSaver("status.txt")  # Especifique o caminho do arquivo de status desejado
    load_status = status_saver.load_status()
    
    pet = Pet(load_status)
    gui = PetGUI(pet, Timer)
    timer = Timer(gui)
    gui.start_button.config(command=timer.start_timer)
    gui.stop_button.config(command=timer.stop_timer)
    video_gui = VideoGUI(gui)
    video_gui.run()
    gui.run()

    status_saver.save_status(pet.hunger, pet.happiness, pet.energy)
if __name__ == "__main__":
    main()
