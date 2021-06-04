import pygame
pygame.init()

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Midpoint Ellipse Drawing Algorithm")
clock = pygame.time.Clock()

window.fill((255,255,255))
point = pygame.PixelArray(window)

def mid_ellipse(x,y,rx,ry):    
 x_new,y_new = 0, ry    #starting point
 while (2*(ry**2)*x_new) <= (2*(rx**2)*y_new): 
  x1,y1 = x_new,y_new
  x2,y2 = x_new,-y_new
  x3,y3 = -x_new,-y_new
  x4,y4 = -x_new,y_new
 
  x1,y1 = x1+x, y1+y 
  x2,y2 = x2+x, y2+y 
  x3,y3 = x3+x, y3+y 
  x4,y4 = x4+x, y4+y  
  
  point[x1][y1] = (0,0,0)
  point[x2][y2] = (0,0,0)
  point[x3][y3] = (0,0,0)
  point[x4][y4] = (0,0,0)


  x_test = x_new + 1
  y_test = y_new - (1/2)
  P = ((ry**2)*(x_test**2)) + ((rx**2)*(y_test**2)) - ((ry**2)*(rx**2))	

  if P < 0:
   x_new = x_new + 1
   y_new = y_new
  else:
   x_new = x_new + 1
   y_new = y_new - 1

 while y_new != 0:
  x1,y1 = x_new,y_new
  x2,y2 = x_new,-y_new
  x3,y3 = -x_new,-y_new
  x4,y4 = -x_new,y_new
 
  x1,y1 = x1+x, y1+y 
  x2,y2 = x2+x, y2+y 
  x3,y3 = x3+x, y3+y 
  x4,y4 = x4+x, y4+y 
  
  point[x1][y1] = (0,0,0)
  point[x2][y2] = (0,0,0)
  point[x3][y3] = (0,0,0)
  point[x4][y4] = (0,0,0)

  x_test = x_new + 0.5
  y_test = y_new - 1
  P = ((ry**2)*(x_test**2)) + ((rx**2)*(y_test**2)) - ((ry**2)*(rx**2))	
 
  if P < 0:
   x_new = x_new + 1
   y_new = y_new - 1
  else:
   x_new = x_new 
   y_new = y_new - 1 

mid_ellipse(200,200,100,80)

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 pygame.display.update()
 clock.tick(70) 
 








