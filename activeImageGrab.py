from PIL import ImageGrab

import time

import os 

def capture_screen():
    while True:
        time.sleep(60)
        screenshot = ImageGrab.grab()

        screenshot.save(os.path.join("screenshots", f"screenshot_{int(time.time())}"))
                
capture_screen()