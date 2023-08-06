# Created to know the mouse position (x, y) at the moment of "ctrl+alt". RomanAnon 2023
import time
import mouse
import keyboard

def wait_for_key_combination(keys):
    print("Press the key combination:", keys)
    while True:
        if keyboard.is_pressed(keys):
            break

while True:
    print("Waiting")
    wait_for_key_combination("ctrl+alt")

    print(mouse.get_position())
    time.sleep(2)