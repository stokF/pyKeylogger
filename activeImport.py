import pyperclip

import time

def log_activeKey():
    recent_value = ""
    while True:
        time.sleep(1)
        activeValue = pyperclip.paste()
        if activeValue != recentValue:
            recentValue = activeValue
            print(f'clipboard content: {recentValue}')
log_activeKey()
