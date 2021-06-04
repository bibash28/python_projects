import pygame

pygame.init()
import time
import random

win = pygame.display.set_mode((900,550))
pygame.display.set_caption("Assignment 1")
clock = pygame.time.Clock()

red = (255,0,0)

boatx,boaty = 230,380
c1x,c1y = 40,200
c2x,c2y = 90,200
c3x,c3y = 140,200
m1x,m1y = 40,300
m2x,m2y = 90,300
m3x,m3y = 140,300

c = 3
m = 3
boatstatus = 0


def message(text):
  font = pygame.font.Font('freesansbold.ttf',35)
  texts = font.render(text,True,red)
  win.blit(texts, (650,80))

def message2(text):
  font = pygame.font.Font('freesansbold.ttf',60)
  texts = font.render(text,True,red)
  win.blit(texts, (300,300))

def messaging():
  global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

  #if anyone on boat then 1 else 0
  if(boatx == 230):
   boatstatus = "True"
  elif(boatx == 380):
   boatstatus = "False"	 
  else:
   boatstatus = " " 

  if c1x == 40:
   c1 = 1
  else:
   c1 = 0  

  if c2x == 90:
   c2 = 1
  else:
   c2 = 0  

  if c3x == 140:
   c3 = 1
  else:
   c3 = 0  

  if m1x == 40:
   m1 = 1
  else:
   m1 = 0  

  if m2x == 90:
   m2 = 1
  else:
   m2 = 0  

  if m3x == 140:
   m3 = 1
  else:
   m3 = 0

  c = c1 + c2 + c3
  m = m1 + m2 + m3  

  

  output = str(m)+"m"+" "+str(c)+"c"+" "+ boatstatus
  message(str(output))


  
 


def make_screen():
 #draw background
 background = pygame.image.load("background.jpg")
 win.blit(background,(0,0))

 boat= pygame.image.load("boat.png")
 win.blit(boat,(boatx,boaty))
 
 c1= pygame.image.load("cannibals.png")
 win.blit(c1,(c1x,c1y))

 c2= pygame.image.load("cannibals.png")
 win.blit(c2,(c2x,c2y))

 c3= pygame.image.load("cannibals.png")
 win.blit(c3,(c3x,c3y)) 

 m1= pygame.image.load("missioniaries.png")
 win.blit(m1,(m1x,m1y))

 m2= pygame.image.load("missioniaries.png")
 win.blit(m2,(m2x,m2y))

 m3= pygame.image.load("missioniaries.png")
 win.blit(m3,(m3x,m3y))

 messaging() 




def step1():
 #1Move 2 cannibals to the r
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c1x,c1y = 260,360
 c2x,c2y = 350,360
 make_screen()
 
 pygame.display.update() 
 time.sleep(1)

 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx <= 380:
   boatx += 1
   c1x+=1
   c2x+=1
   
  messaging() 
  
  if boatx == 380:
    pygame.display.update() 
    time.sleep(1)
    c1x,c1y = 640,200
    c2x,c2y = 690,200
    make_screen()
    step2()

  pygame.display.update()
  clock.tick(500)



def step2():
 #2Move 1 cannibal back to the l
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c2x,c2y = 500,360

 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx >= 230:
   boatx -= 1
   c2x-=1
   
  messaging()

  if boatx == 230:
    pygame.display.update() 
    time.sleep(1)
    c2x,c2y = 90,200
    make_screen()
    step3()

  pygame.display.update()
  clock.tick(500)


def step3():
 #3Move 2 cannibals to the r
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c2x,c2y = 260,360
 c3x,c3y = 350,360

 make_screen()
 pygame.display.update() 
 time.sleep(1)

 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx <= 380:
   boatx += 1
   c2x+=1
   c3x+=1
   
  messaging()
  
  if boatx == 380:
    pygame.display.update() 
    time.sleep(1)
    c3x,c3y = 740,200
    c2x,c2y = 690,200
    make_screen()
    step4()

  pygame.display.update()
  clock.tick(500)



def step4():
 #4Move 1 cannibal back to the l
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c3x,c3y = 410,360
 
 make_screen()
 pygame.display.update() 
 time.sleep(1)

 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx >= 230:
   boatx -= 1
   c3x-=1
   
  messaging()

  if boatx == 230:
    pygame.display.update() 
    time.sleep(1)
    c3x,c3y = 140,200
    make_screen()
    step5()

  pygame.display.update()
  clock.tick(500)





def step5():
 #Move 2 missionaries to the r
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 m1x,m1y = 260,360
 m2x,m2y = 350,360

 make_screen()

 pygame.display.update() 
 time.sleep(1)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx <= 380:
   boatx += 1
   m1x+=1
   m2x+=1
   
  messaging()
  
  if boatx == 380:
    pygame.display.update() 
    time.sleep(1)
    m1x,m1y = 640,300
    m2x,m2y = 690,300
    make_screen()
    step6()

  pygame.display.update()
  clock.tick(500)

def step6():
 #6Move 1 missionary and 1 cannibal back to the l
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 m2x,m2y = 410,360
 c1x,c1y = 500,360
 

 make_screen()

 pygame.display.update() 
 time.sleep(1)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx >= 230:
   boatx -= 1
   c1x-=1
   m2x-=1
   
  messaging()

  if boatx == 230:
    pygame.display.update() 
    time.sleep(1)
    m2x,m2y = 90,300
    c1x,c1y = 40,200
    make_screen()
    step7()

  pygame.display.update()
  clock.tick(500)


def step7():
 #7Move 2 missionaries to the r
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 m2x,m2y = 260,360
 m3x,m3y = 350,360

 make_screen()

 pygame.display.update() 
 time.sleep(1)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx <= 380:
   boatx += 1
   m3x+=1
   m2x+=1
   
  messaging()
  
  if boatx == 380:
    pygame.display.update() 
    time.sleep(1)
    m2x,m2y = 690,300
    m3x,m3y = 740,300
    make_screen()
    step8()

  pygame.display.update()
  clock.tick(500)


def step8():
 #8Move 1 cannibal back to the l
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c2x,c2y = 410,360

 make_screen()

 pygame.display.update() 
 time.sleep(1)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx >= 230:
   boatx -= 1
   c2x-=1
   
  messaging()

  if boatx == 230:
    pygame.display.update() 
    time.sleep(1)
    c2x,c2y = 90,200
    make_screen()
    step9()

  pygame.display.update()
  clock.tick(500)


def step9():
 #9Move 2 cannibals to the r
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c1x,c1y = 260,360
 c2x,c2y = 350,360

 make_screen()

 pygame.display.update() 
 time.sleep(1)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx <= 380:
   boatx += 1
   c1x+=1
   c2x+=1
   
  messaging()
  
  if boatx == 380:
    pygame.display.update() 
    time.sleep(1)
    c1x,c1y = 640,200
    c2x,c2y = 690,200
    make_screen()
    step10()

  pygame.display.update()
  clock.tick(500)

def step10():
 #10Move 1 cannibal back to the l
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c2x,c2y = 500,360
 

 make_screen()

 pygame.display.update() 
 time.sleep(1)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx >= 230:
   boatx -= 1
   c2x-=1
   
  messaging()

  if boatx == 230:
    pygame.display.update() 
    time.sleep(1)
    c2x,c2y = 90,200
    make_screen()
    step11()

  pygame.display.update()
  clock.tick(500)


def step11():
 #11Move 2 cannibals to the r
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c3x,c3y = 260,360
 c2x,c2y = 350,360

 make_screen()

 pygame.display.update() 
 time.sleep(1)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx <= 380:
   boatx += 1
   c3x+=1
   c2x+=1
   
  messaging()
  
  if boatx == 380:
    pygame.display.update() 
    time.sleep(1)
    c3x,c3y = 740,200
    c2x,c2y = 690,200
    make_screen()
    
    pygame.display.update() 
    time.sleep(1)
    message2("Success")
    pygame.display.update() 
    time.sleep(5)
    pygame.quit()
    quit()

  pygame.display.update()
  clock.tick(500)



def step_QW():
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 m1x,m1y = 260,360
 m2x,m2y = 350,360

 make_screen()
 pygame.display.update() 
 time.sleep(1)
 
 message2("Game Over")
 pygame.display.update() 
 time.sleep(5)
 pygame.quit()
 quit()




def stepA():
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c1x,c1y = 260,360
 c2x,c2y = 350,360

 make_screen()

 pygame.display.update() 
 time.sleep(1)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx <= 380:
   boatx += 1
   c1x+=1
   c2x+=1
   
  messaging()
  
  if boatx == 380:
    pygame.display.update() 
    time.sleep(1)
    c1x,c1y = 640,200
    c2x,c2y = 690,200
    make_screen()
    stepB()

  pygame.display.update()
  clock.tick(500)

def stepB():
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c2x,c2y = 500,360
 

 make_screen()

 pygame.display.update() 
 time.sleep(1)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx >= 230:
   boatx -= 1
   c2x-=1
   
  messaging()

  if boatx == 230:
    pygame.display.update() 
    time.sleep(1)
    c2x,c2y = 90,200
    make_screen()
    stepC()

  pygame.display.update()
  clock.tick(500)


def stepC():
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c3x,c3y = 260,360
 c2x,c2y = 350,360

 make_screen()

 pygame.display.update() 
 time.sleep(1)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx <= 380:
   boatx += 1
   c3x+=1
   c2x+=1
   
  messaging()
  
  if boatx == 380:
    pygame.display.update() 
    time.sleep(1)
    c3x,c3y = 740,200
    c2x,c2y = 690,200
    make_screen()
    stepD()
    
    pygame.display.update() 
    time.sleep(10)

  pygame.display.update()
  clock.tick(500)


def stepD():
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 c3x,c3y = 410,360
 c2x,c2y = 500,360
 

 make_screen()

 pygame.display.update() 
 time.sleep(1)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()

  make_screen() 
  if boatx >= 230:
   boatx -= 1
   c3x-=1
   c2x-=1
   
  messaging()

  if boatx == 230:
    pygame.display.update() 
    time.sleep(1)
    c2x,c2y = 90,200
    c3x,c3y = 140,200
    make_screen()
    stepE()

  pygame.display.update()
  clock.tick(500)


def stepE():
 global boatx,c1x,c1y,c2x,c2y,c3x,c3y,m1x,m1y,m2x,m2y,m3x,m3y

 pygame.display.update() 
 time.sleep(1)
 m1x,m1y = 260,360
 m2x,m2y = 350,360

 make_screen()
 pygame.display.update() 
 time.sleep(1)
 
 message2("Game Over")
 pygame.display.update() 
 time.sleep(5)
 pygame.quit()
 quit()




while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()

 make_screen() 
 messaging()

 x = [1,2,3]
 a = random.choice(x)
 print(a)
 if a == 1:
  step1()
 elif a == 2:
  step_QW()
 elif a == 3:
  stepA()

 pygame.display.update()
 clock.tick(500)





 


 

