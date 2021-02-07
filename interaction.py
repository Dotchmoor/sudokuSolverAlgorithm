import win32api, pyautogui

def mouseClick(x, y):
    pyautogui.click(x=x, y=y)    

def moveUp():
    win32api.keybd_event(0x26, 0,0,0)

def moveDown():
    win32api.keybd_event(0x28, 0,0,0)

def moveLeft():
    win32api.keybd_event(0x25, 0,0,0)

def moveRight():
    win32api.keybd_event(0x27, 0,0,0)

def setTo(number):
    numbers = {0:0x30, 1:0x31, 2:0x32, 3:0x33 ,4:0x34,
               5:0x35, 6:0x36, 7:0x37, 8:0x38, 9:0x39}
    win32api.keybd_event(numbers[number], 0,0,0)
