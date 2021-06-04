import pygame
pygame.init()

window = pygame.display.set_mode((200,200))
pygame.display.set_caption("House")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
brown = (244,164,96)

window.fill(white)

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
  
#redefining the pixel
 pixArray = pygame.PixelArray(window)
 pixArray[10][20] = black
 pixArray[10][22] = black
 pixArray[10][24] = black
 pixArray[10][26] = black
 pixArray[10][28] = black 

 for i in range(30,100,3):
  for j in range(1,115,3):
   pixArray[i][j] = blue
 
 pygame.display.update()
 clock.tick(70)
