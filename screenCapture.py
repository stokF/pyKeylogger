from PIL import ImageGrab
import time
import os

def captureScreen():
    while True:
        time.sleep(60)
        screenShot = ImageGrab.grab()
        screenShot.save(os.path.join("screenshots", f"screenShot_{int(time.time())}.png"))