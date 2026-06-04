from pynput import keyboard

def activeKey(key):
    try:
        print(f'Key pressed: {key.char}')
    except AttributeError:
        print(f'Specific key pressed: {key}')

listener = keyboard.Listener(activeKey=activeKey)
listener.start()
listener.join()

        