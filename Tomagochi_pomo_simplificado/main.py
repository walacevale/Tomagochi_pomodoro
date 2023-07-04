import tkinter as tk
from action import Action
from draw import ASCIIImages
from pet import Pet, StatusSaver

status_saver = StatusSaver("status.txt") 
load_status = status_saver.load_status()

pet = Pet(load_status)
draw = ASCIIImages()
action = Action(draw, pet)


action.janela.mainloop()
