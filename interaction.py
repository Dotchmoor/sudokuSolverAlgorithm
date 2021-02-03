import pyautogui

def mouseClick(x, y):
    pyautogui.click(x=x, y=y)    

def moveUp():
    win32api.keybd_event(0x26, 0,0,0)

def moveDown():
    win32api.keybd_event(0x28, 0,0,0)

def moveLeft():
    win32api.keybd_event(0x22, 0,0,0)

def moveRight():
    win32api.keybd_event(0x27, 0,0,0)
