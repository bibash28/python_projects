import pygame
pygame.init()

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Midpoint CIrcle Drawing Algorithm")
clock = pygame.time.Clock()

window.fill((255,255,255))
point = pygame.PixelArray(window)

def mid_circle(x,y,r):
 x0,y0 = 0, r       #starting point
 x_new,y_new = x0,y0    
 P = 1 - r
 while x_new <= y_new:
  x1,y1 = x_new,y_new
  x2,y2 = y_new,x_new
  x3,y3 = x_new,-y_new
  x4,y4 = y_new,-x_new
  x5,y5 = -y_new,-x_new
  x6,y6 = -x_new,-y_new
  x7,y7 = -x_new,y_new
  x8,y8 = -y_new,x_new
 
  x1,y1 = x1+x, y1+y 
  x2,y2 = x2+x, y2+y 
  x3,y3 = x3+x, y3+y 
  x4,y4 = x4+x, y4+y 
  x5,y5 = x5+x, y5+y 
  x6,y6 = x6+x, y6+y 
  x7,y7 = x7+x, y7+y 
  x8,y8 = x8+x, y8+y 
  
  point[x1][y1] = (0,0,0)
  point[x2][y2] = (0,0,0)
  point[x3][y3] = (0,0,0)
  point[x4][y4] = (0,0,0)
  point[x5][y5] = (0,0,0)
  point[x6][y6] = (0,0,0)
  point[x7][y7] = (0,0,0)
  point[x8][y8] = (0,0,0) 

  if P < 0:
   x_new = x_new + 1
   y_new = y_new
   P = P + (2*x_new) + 1
  else:
   x_new = x_new + 1
   y_new = y_new - 1
   P = P + (2*(x_new-y_new)) + 1



mid_circle(200,200,150)
mid_circle(200,200,100)

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 pygame.display.update()
 clock.tick(70) 
 








