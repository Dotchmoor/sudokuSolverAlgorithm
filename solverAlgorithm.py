import interaction, time

class algorithm():
    def __init__(self, gameGrid,):
        self.gameGrid = gameGrid
        self.prePos = []
        for y in range(9):
            for x in range(9):
                if gameGrid[y][x] != 0:
                    self.prePos.append((x, y))

        print(self.prePos)
        self.posX, self.posY = 0, 0
        self.gaps = 0.005
        self.solve()
    
    def solve(self,):
        fieldData = {f"box{i}":{"general":[], "fields":{j:[] for j in range(0,9)}} for i in range(0, 9)}
        print(fieldData)
        #while (self.posX, self.posY) in self.prePos:
        #    self.move()
        #    time.sleep(self.gaps)    
        
        #### remove possible numbers that are in the 3x3 ####
        iBP = {i:None for i in range(1, 10)}
        boxC = 0
        for blockline in range(0, 7, 3):
            for block in range(0, 7, 3):
                inBoxPossible = iBP
                box = 0
                for y in range(0+blockline, 3+blockline):
                    for x in range(0+block, 3+block):
                        if (x, y) in self.prePos:
                            del inBoxPossible[self.gameGrid[y][x]]
                            fieldData[f"box{boxC}"]["general"] = inBoxPossible
                            fieldData[f"box{boxC}"]["fields"][box] = inBoxPossible
                        else:
                            fieldData[f"box{boxC}"]["fields"][box] = iBP
                        box += 1
                boxC += 1



        print(fieldData)

    def move(self,):
        interaction.moveRight()
        self.posX += 1
        
        if self.posX > 8:
            for _ in range(0,8):
                interaction.moveLeft()
                time.sleep(self.gaps)
            interaction.moveDown()
            self.posY += 1
            self.posX = 0

        if self.posY > 8:
            for _ in range(0,8):
                interaction.moveUp()
                time.sleep(self.gaps)
                interaction.moveLeft()
                time.sleep(self.gaps)
            self.posX = 0
            self.posY = 0

    def moveBack(self,):
        for _ in range(0, self.posX):
            interaction.moveLeft()
            time.sleep(self.gaps)
        for _ in range(0, self.posY):
            interaction.moveUp()
            time.sleep(self.gaps)

        self.posX = 0
        self.posY = 0