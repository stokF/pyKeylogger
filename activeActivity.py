import psutil

import pygetwindow as gw 

import time 

def trackActivity():
    previousWindow = None
    while True:
        time.sleep(5)
        
        currentWindow = gw.getActiveWindow()
        if currentWindow != previousWindow:
            previousWindow = currentWindow
            print(f'Active window: {currentWindow}')

        for proc in psutil.process_iter(['pid', 'name']):
            print(f'Running process: {proc.info["name"]} (PID: {proc.info["pid"]})')

            trackActivity()