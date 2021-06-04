import pygame
pygame.init()

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("House")
clock = pygame.time.Clock()

window.fill((255,255,255))
point = pygame.PixelArray(window)

def dda(x1,y1,x2,y2):
 dx = x2 - x1
 dy = y2 - y1
 if abs(dx) > abs(dy):
  stepsize = dx
 else:
  stepsize = dy
 x_inc = dx/stepsize
 y_inc = dy/stepsize
 x_new = x1
 y_new = y1
 
 for i in range(1,abs(stepsize)+1):
  point[round(x_new)][round(y_new)] = (0,0,0)
  print(x_new,y_new)
  x_new = x_new + x_inc
  y_new = y_new + y_inc

dda(10,10,10,380)
dda(10,380,380,380)

dda(40,200,150,130)
dda(150,130,240,135)
dda(240,135,330,165)

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 pygame.display.update()
 clock.tick(70)
