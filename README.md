# Basic Keylogger (Educational Use Only)

This is a simple keylogger tool developed using Python and the `pynput` library. It was created strictly for educational purposes as part of a cybersecurity internship project.

The script listens for keyboard inputs and logs them — along with timestamps — to a local file named `keylog.txt`. This project is intended to demonstrate how basic keylogging works in a safe, legal, and permission-granted environment.

⚠️ Ethical Disclaimer: This tool must not be used for any unauthorized or malicious activity. Unauthorized use of keyloggers is illegal and unethical. Always get explicit permission before using monitoring tools.

Features:
- Logs all keyboard input
- Includes timestamps for each keypress
- Handles both regular and special keys
- Press `ESC` to stop logging

Installation:
Make sure Python is installed. Then install the required package:
pip install pynput

Usage:
Run the script in a terminal or command prompt:
python keylogger.py

All logs will be saved to a file named `keylog.txt` in the same directory.

License:
This project is licensed under the MIT License. You are free to use, modify, and share this code under the terms of that license.
