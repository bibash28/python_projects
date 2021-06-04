import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

win = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Race Car')
clock = pygame.time.Clock()

car_width = 54
car = pygame.image.load('car.png') #import car

def cars(a,b):
 win.blit(car,(a,b)) #blit -> like drawing to background

def crash():
 message('You Crashed')

def message(text):
 fontObj = pygame.font.Font('freesansbold.ttf',112) #name,size
 textSurfaceObj = fontObj.render(text,True, black)
 textRectObj = textSurfaceObj.get_rect()
 textRectObj.center = (400, 300)
 win.blit(textSurfaceObj, textRectObj)
 pygame.display.update()
 time.sleep(2)
 game_loop()

def things_dodged(count):
 font = pygame.font.Font(None,32) #name,size
 text = font.render("Score: "+ str(count),True,black)
 win.blit(text,(1,1))


def things(thingx, thingy, thingw, thingh, color):
 pygame.draw.rect(win, color,[thingx,thingy, thingw, thingh])

def game_loop():
 #top left is (0,0)... x right y up
 x = 400
 y = 450
 x_new = 0

 thing_startx = random.randrange(0, display_width)
 thing_starty = -600
 thing_speed = 7
 thing_width = 75
 thing_height = 100
 
 dodged = 0 

 running = True
 while running:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()
   if event.type == pygame.KEYDOWN: #keydown -> push key
    if event.key == pygame.K_LEFT:
     x_new = -5
    elif event.key == pygame.K_RIGHT: #keyup -> release key
     x_new = 5

   if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
     x_new = 0

  x += x_new
  win.fill(white)

  things(thing_startx, thing_starty, thing_width, thing_height, random.choice([black,green,red]))
  thing_starty += thing_speed
  cars(x,y)
  things_dodged(dodged)

  #setting boundary to car
  if x > display_width - car_width or x < 0:
   crash()

  if thing_starty > display_height:
   thing_starty = 0 - thing_height
   thing_startx = random.randrange(0,display_width-thing_width)
   dodged += 1 
   thing_speed += 0.3
   
  if y < thing_starty + thing_height: #crosses car from top
    if x > thing_startx and x < thing_startx + thing_width:
     crash()
    elif x+car_width > thing_startx and x+car_width < thing_startx + thing_width:
     crash()
  pygame.display.update()
  clock.tick(80)

game_loop()



