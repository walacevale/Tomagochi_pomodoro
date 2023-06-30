from pet import Pet
from gui import PetGUI
from timer import Timer
from video_gui import VideoGUI

def main():
    pet = Pet()
    gui = PetGUI(pet, Timer)
    timer = Timer(gui)
    gui.start_button.config(command=timer.start_timer)
    gui.stop_button.config(command=timer.stop_timer)
    video_gui = VideoGUI(gui)
    video_gui.run()
    gui.run()


if __name__ == "__main__":
    main()