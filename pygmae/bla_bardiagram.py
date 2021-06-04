import pygame
pygame.init()

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("BLA Algorithm")
clock = pygame.time.Clock()

window.fill((255,255,255))
point = pygame.PixelArray(window)

def bla(x1,y1,x2,y2):
 dx = x2 - x1
 dy = y2 - y1

 x_new = x1
 y_new = y1

 if abs(dy) < abs(dx):
  P = (2*dy) - dx
  while x_new != x2:
   point[x_new][y_new] = (0,0,0)
   x_new = x_new + 1
   if P < 0:
    y_new = y_new
    P =  P + (2*dy)
   else:
    y_new = y_new + 1
    P = P + (2*dy) - (2*dx)
 else:
  P = (2*dx) - dy
  while y_new != y2:
   point[x_new][y_new] = (0,0,0)
   y_new = y_new + 1
   if P < 0:
    x_new = x_new
    P =  P + (2*dx)
   else:
    x_new = x_new + 1 
    P = P + (2*dx) - (2*dy)

bla(10,10,10,380)
bla(10,380,380,380)

bla(60,280,60,380)
bla(60,280,120,280)
bla(120,280,120,380)

bla(180,180,180,380)
bla(180,180,240,180)
bla(240,180,240,380)

bla(300,80,300,380)
bla(300,80,360,80)
bla(360,80,360,380)



while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 pygame.display.update()
 clock.tick(100)

