import pygame
from tkinter import *
from tkinter import messagebox

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1050,500))
pygame.display.set_caption("Missionary and cannibal")
background = pygame.image.load("board.jpg")
background = pygame.transform.scale(background,(1200,500))
screen.blit(background,(0,0))
done = False
canObj = [None]*3
misObj = [None]*3
cPosXL = [80,120,160]
mPosXL = [200,240,280]
cPosXR = [800,850,890]
mPosXR = [930,970,1010]
button = pygame.image.load("button.png")
button = pygame.transform.scale(button,(100,50))


class boatClass:
    position = "Left"
    capacity = 2
    occupied = 0
    posX = 300
    posY = 315
    image = pygame.image.load("boat.png")
    image = pygame.transform.scale(image,(200,80))

    def displayImage(self):
        screen.blit(self.image,(self.posX,self.posY))

class cannibal:
    posX = 0
    posY = 0
    position = "Left"
    selected = False
    ontheBoat = False
    image = pygame.image.load("can.png")
    image = pygame.transform.scale(image,(35,60))

    def changeBoat(self):
        if self.ontheBoat == False:
            self.ontheBoat = True
        else:
            self.ontheBoat = True

    def displayImage(self):
        screen.blit(self.image,(self.posX,self.posY))

class missionary:
    posX = 0
    posY = 0
    position = "Left"
    selected = False
    ontheBoat = False
    image = pygame.image.load("mission.png")
    image = pygame.transform.scale(image,(35,60))

    def changeBoat(self):
        if self.ontheBoat == False:
            self.ontheBoat = True
        else:
            self.ontheBoat = True

    def displayImage(self):
        screen.blit(self.image,(self.posX,self.posY))



def init():
    global boat
    boat = boatClass()
    for i in range(3):
        canObj[i] = cannibal()
        misObj[i] = missionary()
        canObj[i].posX = cPosXL[i]
        canObj[i].posY = 250
        misObj[i].posX = mPosXL[i]
        misObj[i].posY = 250
    displayImages()


def displayImages():
    screen.blit(background,(0,0))
    for i in range(3):
        canObj[i].displayImage()
        misObj[i].displayImage()
    boat.displayImage()
    screen.blit(button,(480,400))

def changeBoat():
    for i in range(3):
        if canObj[i].selected == True:
            if canObj[i].ontheBoat == False:
                canObj[i].ontheBoat = True
                if boat.occupied == 0:
                    canObj[i].posX = boat.posX +30
                else:
                    canObj[i].posX = boat.posX + 80
                canObj[i].posY = boat.posY - 30
                boat.occupied+=1
                break
            elif canObj[i].ontheBoat == True:
                boat.occupied-=1
                if canObj[i].position == "Left":
                    canObj[i].posX = cPosXL[i]
                else:
                    canObj[i].posX = cPosXR[i]
                canObj[i].posY = 250
                canObj[i].ontheBoat = False
                break
    for i in range(3):
        if misObj[i].selected == True:
            if misObj[i].ontheBoat == False:
                misObj[i].ontheBoat = True
                if boat.occupied == 0:
                    misObj[i].posX = boat.posX +30
                else:
                    misObj[i].posX = boat.posX + 80
                misObj[i].posY = boat.posY - 30
                boat.occupied +=1
                break
            elif misObj[i].ontheBoat == True:
                boat.occupied -=1
                if misObj[i].position == "Left":
                    misObj[i].posX = mPosXL[i]
                else:
                    misObj[i].posX = mPosXR[i]
                misObj[i].posY = 250
                misObj[i].ontheBoat = False
                break

def gameOver():
    global done
    Tk().wm_withdraw()
    messagebox.showinfo("Game Over","Cannibal has eaten the missionary")
    done = True

def winstate():
    Tk().wm_withdraw()
    messagebox.showinfo("Winner","You have successfully transferred them to other shore")

def checkLeftSide():
    canNum = 0
    misNum = 0
    for i in range(3):
        if(canObj[i].position == "Left"):
            canNum +=1
        if(misObj[i].position == "Left"):
            misNum +=1
    print(canNum,misNum)
    if canNum > misNum and misNum!=0:
        gameOver()

def checkRightSide():
    canNum = 0
    misNum = 0
    for i in range(3):
        if(canObj[i].position == "Right"):
            canNum +=1
        if(misObj[i].position == "Right"):
            misNum +=1
    print(canNum,misNum)
    if canNum > misNum and misNum!=0:
        gameOver()
    if canNum == 3 and misNum == 3:
        winstate()


def animate():
    start = boat.position
    if start == "Left":
        for j in range(boat.posX,700):
            boat.posX = j
            for i in range(3):
                if canObj[i].ontheBoat == True:
                    canObj[i].posX +=1
                    canObj[i].position = "Right"
                if misObj[i].ontheBoat == True:
                    misObj[i].posX +=1
                    misObj[i].position = "Right"

            displayImages()
            clock.tick(60)

            pygame.display.flip()
        boat.position = "Right"
    elif start == "Right":
        for i in range(boat.posX,300,-1):
            boat.posX = i
            for i in range(3):
                if canObj[i].ontheBoat == True:
                    canObj[i].posX -=1
                    canObj[i].position = "Left"
                if misObj[i].ontheBoat == True:
                    misObj[i].posX -=1
                    misObj[i].position = "Left"

            displayImages()
            clock.tick(60)
            pygame.display.flip()
        boat.position = "Left"
    checkLeftSide()
    checkRightSide()





init()
while not done:
    buttonClick = pygame.event.poll()
    if buttonClick.type == pygame.QUIT:
        done = True
    if buttonClick.type == pygame.MOUSEBUTTONDOWN:
        x,y = buttonClick.pos
        if button.get_rect(topleft=(480,400)).collidepoint(x,y) and boat.occupied != 0:
            animate()
        for i in range(3):
            if canObj[i].image.get_rect(topleft=(canObj[i].posX,canObj[i].posY)).collidepoint(x,y):
                canObj[i].selected = True
                changeBoat()
                canObj[i].selected = False
            elif misObj[i].image.get_rect(topleft=(misObj[i].posX,misObj[i].posY)).collidepoint(x,y):
                misObj[i].selected = True
                changeBoat()
                misObj[i].selected = False

            displayImages()


            pygame.display.flip()
    clock.tick(60)
    pygame.display.flip()
