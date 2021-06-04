import pygame
import os

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("BagChaal")
background = pygame.image.load("board.png")
emptyImage = pygame.image.load("blank.png")
screen.blit(background,(0,0))
done = False
gridXPos = [234,392,549,707,865]
gridYPos = [11,162,315,479,620]
goatTurn = True
tigerTurn = False
goat = [None]*20
fox = [None]*4
box = [None]*25
currentBox = 0
newBox = 0
deadGoat = 0
deadTiger = 0
global firstGoatMove



class gridBox:
    boxid = 0
    PosX = 0
    PosY = 0
    elligibleBox = []
    killElligibleBox = []
    occupied = False
    occupiedBy = "Empty"
    image = pygame.image.load("blank.png")

    def setOccupy(self,occupied):
        self.occupied = occupied

    def initPos(self,x,y):
        self.PosX = x
        self.PosY = y

    def setBlank(self):
        screen.blit(self.image,(self.PosX,self.PosY))

class goatObj:
    PosX = 0
    PosY = 0
    selected = False
    intheBox = False
    status = "alive"
    boxid = 100
    firstMove = True
    global image

    def initPos(self,x,y):
        self.PosX = x
        self.PosY = y

    def selectImage(self):
        if self.status == "alive":
            if not self.selected:
                self.image = pygame.image.load("goat.png")
            else:
                self.image = pygame.image.load("goat_selected.png")
        else:
            self.image = pygame.image.load("goat_out.png")

    def displayPos(self):
        self.selectImage()
        screen.blit(self.image,(self.PosX,self.PosY))

    def setStatus(self,status):
        self.status = status

    def setSelection(self,selection):
        self.selected = selection


class foxObj:
    PosX = 0
    PosY = 0
    boxid = 0
    selected = False
    status = "alive"
    image = pygame.image.load("tiger.png")


    def selectImage(self):
        if self.status == "alive":
            if not self.selected:
                image = pygame.image.load("tiger.png")
            else:
                image = pygame.image.load("tiger_selected.png")
        else:
            image = pygame.image.load("tiger_trapped.png")

    def initPos(self,x,y):
        self.PosX = x
        self.PosY = y


    def displayPos(self):
        self.selectImage()
        screen.blit(self.image,(self.PosX,self.PosY))

    def setStatus(self,status):
        self.status = status

    def setSelection(self,selection):
        self.selected = selection

def setElligibilty():
    box[0].elligibleBox = [1,5,6]
    box[1].elligibleBox = [0,2,5,6,7]
    box[2].elligibleBox = [1,3,6,7,8]
    box[3].elligibleBox = [2,4,7,8,9]
    box[4].elligibleBox = [3,8,9]
    box[5].elligibleBox = [0,1,6,10,11]
    box[6].elligibleBox = [0,1,2,5,7,10,11,12]
    box[7].elligibleBox = [2,6,8,12]
    box[8].elligibleBox = [2,3,4,7,9,12,13,14]
    box[9].elligibleBox = [4,8,14]
    box[10].elligibleBox = [5,6,11,15,16]
    box[11].elligibleBox = [6,10,12,16]
    box[12].elligibleBox = [6,7,8,11,13,16,17,18]
    box[13].elligibleBox = [8,12,14,18]
    box[14].elligibleBox = [8,9,13,18,19]
    box[15].elligibleBox = [10,16,20]
    box[16].elligibleBox = [10,11,12,15,17,20,21,22]
    box[17].elligibleBox = [12,16,18,22]
    box[18].elligibleBox = [12,13,14,17,19,22,23,24]
    box[19].elligibleBox = [14,18,24]
    box[20].elligibleBox = [15,16,21]
    box[21].elligibleBox = [16,20,22]
    box[22].elligibleBox = [16,17,18,21,23]
    box[23].elligibleBox = [18,22,24]
    box[24].elligibleBox = [18,19,23]

    box[0].killElligibleBox = [2,10,12]
    box[1].killElligibleBox = [3,11]
    box[2].killElligibleBox = [0,4,10,12,14]
    box[3].killElligibleBox = [1,13]
    box[4].killElligibleBox = [2,12,14]
    box[5].killElligibleBox = [7,15]
    box[6].killElligibleBox = [8,16,18]
    box[7].killElligibleBox = [5,9,17]
    box[8].killElligibleBox = [16,18]
    box[9].killElligibleBox = [7,19]
    box[10].killElligibleBox = [0,2,12,20,22]
    box[11].killElligibleBox = [1,13,21]
    box[12].killElligibleBox = [0,2,4,10,14,20,22,24]
    box[13].killElligibleBox = [3,11,23]
    box[14].killElligibleBox = [2,4,12,22,24]
    box[15].killElligibleBox = [5,17]
    box[16].killElligibleBox = [6,8,18]
    box[17].killElligibleBox = [7,15,19]
    box[18].killElligibleBox = [6,8,16]
    box[19].killElligibleBox = [9,17]
    box[20].killElligibleBox = [10,12,22]
    box[21].killElligibleBox = [11,23]
    box[22].killElligibleBox = [10,12,14,20,24]
    box[23].killElligibleBox = [13,21]
    box[24].killElligibleBox = [12,14,22]


def initGrid():
    gridXPos = [234,392,549,707,865]
    gridYPos = [11,162,315,479,620]
    for i in range(25):
        box[i] = gridBox()
        box[i].boxid = i


    k = 0
    for i in range(5):
        for j in range(5):
            box[k].initPos(gridXPos[j],gridYPos[i])
            k = k + 1


    box[0].setOccupy(True)
    box[0].occupiedBy = "fox"
    box[1].setOccupy(True)
    box[1].occupiedBy = "fox"
    box[2].setOccupy(True)
    box[2].occupiedBy = "fox"
    box[3].setOccupy(True)
    box[3].occupiedBy = "fox"



def initGoat():
    posX = [77,1020]
    posY = [8,84,161,237,313,389,465,540,616,693]

    for i in range(20):
        goat[i] = goatObj()
    k = 0
    for i in range(2):
        for j in range(10):
            goat[k].initPos(posX[i],posY[j])
            k = k + 1
    setElligibilty()


def initFox():
    posX=[234,865]
    posY=[11,620]

    for i in range(4):
        fox[i] = foxObj()
    k = 0
    for i in range(2):
        for j in range(2):
            fox[k].initPos(posX[i],posY[j])
            k = k + 1
    fox[0].boxid = 0
    fox[1].boxid = 4
    fox[2].boxid = 20
    fox[3].boxid = 24

def setImages():
    for i in range(25):
        box[i].setBlank()
    for i in range(20):
        goat[i].displayPos()
    for i in range(4):
        fox[i].displayPos()

initGrid()
initGoat()
initFox()
setImages()


def tigerMove():
        goatlist=[]
        foxlist = []
        preyed = False
        global goatTurn
        for j in range(25):
            if box[j].occupiedBy =="goat":
                goatlist.append(j)
            elif box[j].occupiedBy == "fox":
                foxlist.append(j)
        for i in range(4):
            if preyed == False:
                for k in range(len(goatlist)):
                    if goatlist[k] in box[foxlist[i]].elligibleBox and preyed == False:
                        for m in range(len(box[foxlist[i]].killElligibleBox)):
                            if box[box[foxlist[i]].killElligibleBox[m]].occupied == False and preyed == False:
                                if box[foxlist[i]].killElligibleBox[m] in box[goatlist[k]].elligibleBox and preyed == False:
                                    for n in range(4):
                                        if fox[n].boxid == foxlist[i]  and preyed == False:
                                            fox[n].PosX = box[box[foxlist[i]].killElligibleBox[m]].PosX
                                            fox[n].PosY = box[box[foxlist[i]].killElligibleBox[m]].PosY
                                            box[fox[n].boxid].occupied = False
                                            box[fox[n].boxid].occupiedBy = "Empty"
                                            fox[n].boxid = box[foxlist[i]].killElligibleBox[m]
                                            box[fox[n].boxid].occupied = True
                                            box[fox[n].boxid].occupiedBy = "fox"
                                            for r in range(20):
                                                if goat[r].boxid == goatlist[k]:
                                                    goat[r].PosX = 1000
                                                    goat[r].PosY = 1000
                                                    goat[r].status = "dead"
                                                    box[goat[r].boxid].occupied = False
                                                    box[goat[r].boxid].occupiedBy = "Empty"
                                            goatTurn = True
                                            preyed = True
                                            screen.blit(background,(0,0))
                                            setImages()
                                            pygame.display.flip()
                                            break
        if preyed == False:
            moved = False
            for b in range(4):
                if moved == False:
                    for c in range(len(box[fox[b].boxid].elligibleBox)):
                        if box[box[fox[b].boxid].elligibleBox[c]].occupied == False:
                            fox[b].PosX = box[box[fox[b].boxid].elligibleBox[c]].PosX
                            fox[b].PosY = box[box[fox[b].boxid].elligibleBox[c]].PosY
                            box[fox[b].boxid].occupied = False
                            box[fox[b].boxid].occupiedBy = "Empty"
                            fox[b].boxid = box[fox[b].boxid].elligibleBox[c]
                            box[fox[b].boxid].occupied = True
                            box[fox[b].boxid].occupiedBy = "fox"

                            moved = True
                            goatTurn = True
                            screen.blit(background,(0,0))
                            setImages()
                            pygame.display.flip()
                            break





while not done:
    for event in pygame.event.get():
     if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == K_ESCAPE):
       done = True
     if event.type == pygame.MOUSEBUTTONUP:
        x,y = event.pos
        print(x,y)
        if goatTurn == True:
            print(x,y)
            for i in range(20):
                if goat[i].image.get_rect(topleft=(goat[i].PosX,goat[i].PosY)).collidepoint(x,y) and goat[i].intheBox==False:
                    print(x,y)
                    goat[i].setSelection(True)
                    if not goat[i].firstMove:
                        currentBox = goat[i].boxid
                        print(currentBox)
                    goat[i].displayPos()
                    pygame.display.flip()
                    clicked = False
                    while not clicked:
                      for event in pygame.event.get(): 
                        if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == K_ESCAPE):
                          done = true
                        if event.type == pygame.MOUSEBUTTONUP:
                            x1,y2 = event.pos
                            for j in range(25):
                                if box[j].image.get_rect(topleft=(box[j].PosX,box[j].PosY)).collidepoint(x1,y2):
                                    newBox = box[j].boxid
                                    if newBox in box[currentBox].elligibleBox or goat[i].firstMove:
                                        if box[j].occupied == False:
                                            print(goat[i].PosX,goat[i].PosY)
                                            goat[i].initPos(box[j].PosX,box[j].PosY)
                                            goat[i].setSelection(False)
                                            box[j].setOccupy(True)
                                            box[j].occupiedBy = "goat"
                                            goat[i].intheBox = True
                                            print(box[j].boxid)
                                            goat[i].boxid = box[j].boxid
                                            clicked = True
                                            if not goat[i].firstMove:
                                                box[currentBox].occupied = False
                                                box[currentBox].occupiedBy = "Empty"
                                            goat[i].firstMove = False
                                            goatTurn = False

    screen.blit(background,(0,0))
    setImages()
    pygame.display.flip()
    if goatTurn == False:
        tigerMove()
    
