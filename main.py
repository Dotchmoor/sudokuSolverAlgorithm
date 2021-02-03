import win32api, win32gui, time, cv2, numpy, os, sudokuRecognition
from PIL import ImageGrab

sudokuField = [[0 for _ in range(0, 9)] for _ in range(0, 9)]
time.sleep(2)

#### get the image ####
print("now click top left corner above sudoku")
while not win32api.GetAsyncKeyState(0x01):
    global x, y
    x, y = win32gui.GetCursorPos()

time.sleep(3)
print("now click bottom right corner under sudoku")
while not win32api.GetAsyncKeyState(0x01):    
    global width, height
    width, height = win32gui.GetCursorPos()

time.sleep(0.25)

loopTime = time.time()
#### work with the image ####
img =  cv2.cvtColor(numpy.array(ImageGrab.grab(bbox=(x, y, width, height)), ), cv2.COLOR_BGR2RGB).reshape(height-y, width-x, 3).astype(numpy.uint8)

imgPath = os.path.dirname(__file__)
numbers = {"0":cv2.imread(os.path.join(imgPath, "images\\blank.png")).astype(numpy.uint8), "1":cv2.imread(os.path.join(imgPath, "images\\one.png")).astype(numpy.uint8), "2":cv2.imread(os.path.join(imgPath, "images\\two.png")).astype(numpy.uint8),
           "3":cv2.imread(os.path.join(imgPath, "images\\three.png")).astype(numpy.uint8), "4":cv2.imread(os.path.join(imgPath, "images\\four.png")).astype(numpy.uint8), "5":cv2.imread(os.path.join(imgPath, "images\\five.png")).astype(numpy.uint8),
           "6":cv2.imread(os.path.join(imgPath, "images\\six.png")).astype(numpy.uint8), "7":cv2.imread(os.path.join(imgPath, "images\\seven.png")).astype(numpy.uint8), "8":cv2.imread(os.path.join(imgPath, "images\\eight.png")).astype(numpy.uint8),
           "9":cv2.imread(os.path.join(imgPath, "images\\nine.png")).astype(numpy.uint8)}
del x, y, width, height

#### crop image ####
img = sudokuRecognition.imageCrop(img)

##### number recognition #####

fieldSize = 54
posX, posY = 2, 2
impartNum = 0
for line in range(0, 9):
    for number in range(0,9):
        imgPart = img[posY:posY+fieldSize,posX:posX+fieldSize]
        cv2.imwrite(f"data\\impart{impartNum}.png", imgPart)
        treshold = 1.0
        loc = []
        end = False
        while len(loc) < 1 or not end:
            for key, val in numbers.items():
                result = cv2.matchTemplate(val, imgPart, cv2.TM_CCOEFF_NORMED)
                
                loc = list(zip(*numpy.where(result >= treshold)[::-1]))

                if len(loc) > 0:
                    sudokuField[line][number] = int(key)
                    end = True
                    break
        
                treshold -= 0.01

        posX += fieldSize + 1
        if number == 2 or number == 5:
            posX += 1
        impartNum += 1
    posY += fieldSize +1
    if line == 2 or line == 5:
        posY += 1
    posX = 2

print(sudokuField)
print(f"time: {time.time()-loopTime}")

cv2.imshow("window", img)

cv2.waitKey(0)

#win32api.keybd_event(0x27, 0,0,0)
