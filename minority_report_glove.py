# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import serial
import sys
import threading
import time
import pyautogui
import pynput.keyboard
from pynput.keyboard import Key, Controller

keyboard = Controller()
mySerial = serial.Serial('COM8', 9600)

keyBoardKeys = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

def control():
    if(not mySerial.isOpen()):
        mySerial.open()
    while mySerial.isOpen():
        try:
            i = mySerial.inWaiting() #Get the number of bytes in the input buffer --> We willen enkel het laatste commando uitlezen
            dataIn = ""
            dataIn += mySerial.read(i).decode()
            moveCar(dataIn.strip().rstrip()) #remove whitespace characters and new lines
            time.sleep(0.250)
        except:
            raise #allow a caller to handle the exception
        

def moveCar(input):
    print("_______________")
    print(input)
    if input == "gewoonVooruit":
        print("gewoonVooruit")
        keyboard.release(Key.left)
        keyboard.release(Key.right)
        keyboard.press(Key.up)
        keyboard.release(Key.down)
    elif input == "gewoonLinks":
        print("gewoonLinks")
        keyboard.release(Key.up)
        keyboard.release(Key.down)
        keyboard.press(Key.left)
        keyboard.release(Key.right)
    elif input == "gewoonRechts":
        print("gewoonRechts")
        keyboard.release(Key.up)
        keyboard.release(Key.down)
        keyboard.press(Key.right)
        keyboard.release(Key.left)
    elif input == "gewoonAchteruit":
        print("gewoonAchteruit")
        keyboard.release(Key.right)
        keyboard.release(Key.left)
        keyboard.press(Key.down)
        keyboard.release(Key.up)
    elif input == "rechtsVooruit":
        print("rechtsVooruit")
        keyboard.press(Key.up)
        keyboard.release(Key.down)
        keyboard.press(Key.right)
        keyboard.release(Key.left)
    elif input == "rechtsAchteruit":
        print("rechtsAchteruit")
        keyboard.press(Key.down)
        keyboard.release(Key.up)
        keyboard.press(Key.right)
        keyboard.release(Key.left)
    elif input == "linksVooruit":
        print("linksVooruit")
        keyboard.press(Key.up)
        keyboard.release(Key.down)
        keyboard.press(Key.left)
        keyboard.release(Key.right)
    elif input == "linksAchteruit":
        print("linksAchteruit")
        keyboard.press(Key.down)
        keyboard.release(Key.up)
        keyboard.release(Key.right)
        keyboard.press(Key.left)
    elif input == "stil":
        print("stil")
        keyboard.release(Key.down)
        keyboard.release(Key.up)
        keyboard.release(Key.left)
        keyboard.release(Key.right)
    else:
        keyboard.release(Key.down)
        keyboard.release(Key.up)
        keyboard.release(Key.left)
        keyboard.release(Key.right)
        


if __name__ == "__main__":
    try:
        th = threading.Thread(target = control)
        th.deamon = True #set thread as a deamon thread
        th.start() #start deamon thread
        print("______STARTED______1052")
        while True: time.sleep(100)
    except(KeyboardInterrupt, Exception):
        mySerial.close()
        raise
    sys.exit()