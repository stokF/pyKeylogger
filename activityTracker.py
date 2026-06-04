import psutil
import pygetwindow as gw
import time

def trackActivity():
    previousWindow = None
    while True:
        time.sleep(5)
        currentWindow = gw.getActiveWindowTitle()
        if currentWindow != previousWindow:
            previousWindow = currentWindow
            with open("logs/activityLog.txt", "a") as logFile:
                logFile.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {currentWindow}\n')
        for proc in psutil.process_iter(['pid', 'name']):
            with open("logs/processLog.txt", "a") as logFile:
                logFile.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {proc.info["name"]} (PID: {proc.info["pid"]})\n')