import time
import random
import keyboard
import mouse

START = -111

def press(key):
    keyboard.send(key)
    time.sleep(random.uniform(.025,.035))

def cold_snap():        press("q"); press("q"); press("q")
def ghost_walk():       press("w"); press("q"); press("q")
def tornado():          press("w"); press("q"); press("w")
def emp():              press("w"); press("w"); press("w")
def alacrity():         press("w"); press("w"); press("e")
def chaos_meteor():     press("w"); press("e"); press("e")
def sun_strike():       press("e"); press("e"); press("e")
def forge_spirit():     press("e"); press("e"); press("q")
def ice_wall():         press("q"); press("q"); press("e")
def deafening_blast():  press("e"); press("q"); press("w")

def spell():
    time.sleep(random.uniform(0.02, 0.04))
    press("r")
    time.sleep(random.uniform(0.02, 0.04))
    press("d")
    time.sleep(random.uniform(0.08, 0.12))
    mouse.click("left")

def full_combo():
    global START
    if START is not -111 and (time.time() - START) < 5:
        return
    START = time.time()
    chaos_meteor()
    spell()
    time.sleep(random.uniform(0.4, 0.5))
    deafening_blast()
    spell()
    cold_snap()
    spell()
    forge_spirit()
    spell()
    emp()
    spell()

keyboard.add_hotkey("=", full_combo)
print("Script is ready. Press '=' to start")
keyboard.wait("")
