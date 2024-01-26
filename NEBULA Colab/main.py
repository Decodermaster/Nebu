import eel
from MAIN.Nebula import *

eel.init("DESIGN")

@eel.expose
def start_nebula():
    
    while True:
        if hot.hotword_detection():
            print("Hotword detected")
            TaskExicution()
        # if mouse is True:
        #     off.mousemove()
            
eel.start('index.html')