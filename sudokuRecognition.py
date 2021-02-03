import cv2, numpy

def imageCrop(img):
    for y in range(0, 100):
        if img[y][50][0] != 255: 
            global cropY
            cropY = y
            break

    for x in range(0, 100):
        if img[50][x][0] != 255: 
            global cropX
            cropX = x
            break

    for yM in range(1, 100):
        if img[50][-yM][0] != 255: 
            global cropHeight
            cropHeight = len(img)-yM
            break

    for xM in range(1, 100):
        if img[50][-xM][0] != 255: 
            global cropWidth
            cropWidth = len(img[0])-xM
            break

    return img[cropY:(cropY+cropHeight)-1, cropX:(cropX+cropWidth)]


def numberRecognition(img, templateDict, fieldSize, startShift):
    sudokuField = [[0 for _ in range(0, 9)] for _ in range(0, 9)]

    posX, posY = startShift, startShift
    for line in range(0, 9):
        for number in range(0,9):
            imgPart = img[posY:posY+fieldSize,posX:posX+fieldSize]
            treshold = 1.0
            loc = []
            end = False
            while len(loc) < 1 or not end:
                for key, val in templateDict.items():
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
        posY += fieldSize +1
        if line == 2 or line == 5:
            posY += 1
        posX = 2

    return sudokuField