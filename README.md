# PRODIGY_CY_04
Task 04: Keylogger Program
This project is an educational demonstration of a keylogger program created as part of an internship task at Prodigy Infotech. It combines the functionality of both the pynput and keyboard Python modules to capture and log keystrokes to a file.

Overview:
The program records keystrokes and writes them to a text file named keystrokes.txt. The design ensures that both alphanumeric and special keys are captured. Ethical considerations and necessary permissions are essential when working with keyloggers, even for learning purposes.

Key Features:
Real-Time Keystroke Logging: Captures keystrokes using pynput and logs them to keystrokes.txt.
Threaded Listener: Implements a multi-threaded approach to ensure the keyboard listener from the keyboard module runs concurrently.
Supports Special Keys: Captures both printable characters and special keys like Shift, Ctrl, etc.
Exit Mechanism: Stops recording when the Escape key is pressed.
Code Highlights:
Uses threading to run the keyboard module listener alongside the pynput listener.
Stores each keypress in a human-readable format in the output file.
Demonstrates error handling for file I/O operations.
Usage Notice:
This project is intended solely for educational purposes to understand keylogging concepts. Always ensure compliance with legal and ethical standards when using or sharing such tools.
