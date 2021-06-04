import pygame
pygame.init()
import time

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Cohen Sutherland LDA")
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

window.fill(white)

def setcode(x,y,xwmin,ywmin,xwmax,ywmax):
 a = [0,0,0,0]
 if x < xwmin:   #left(top in computer)
  a = '1'
 else:
  a = '0'
 if x > xwmax:   #right
  b = '1'
 else:
  b = '0'
 if y < ywmin:   #bottom
  c = '1'
 else:
  c = '0'
 if y > ywmax:   #top(bottom in computer)
  d = '1'
 else:
  d = '0'
 return str(a+b+c+d)
 
def cohen_sutherland_algo(x1,y1,x2,y2):
 #clipping window
 xwmin,ywmin = 50, 50
 xwmax,ywmax = 100, 100
 pygame.draw.polygon(window,black,((50,50),(100,50),(100,100),(50,100)),1)  #(initialpoints, length)

 m = (y2-y1)/(x2-x1)
 pygame.draw.line(window,black,(x1,y1),(x2,y2),1)

 a = setcode(x1,y1,xwmin,ywmin,xwmax,ywmax)
 b = setcode(x2,y2,xwmin,ywmin,xwmax,ywmax)
 print(a,b)
 if a == '0000' and b =='0000':
  print('Completely inside')
  pass
 else:
  c = str((int(a[0]) & int(b[0]))) + str((int(a[1]) & int(b[1]))) + str((int(a[2]) & int(b[2]))) + str((int(a[3]) & int(b[3]))) 
  if c != '0000':
   print('completely outside')
   pass
  else:
   if  a != '0000' and b !='0000':
    print('intersection')
    y11 = ywmax
    x11 = x1 + ((y11-y1)/m)
    x21 = xwmax
    y21 = y1 + (m*(x21-x1))
   elif a == '0000' and b !='0000':
    y11 = y1
    x11 = x1
    x21 = xwmax
    y21 = y1 + (m*(x21-x1))   
   elif a == '0000' and b =='0000':
    y11 = ywmax
    x11 = x1 + ((y11-y1)/m)
    x21 = x2
    y21 = y2   
  pygame.display.update()
  time.sleep(1)  
  window.fill(white) 
  pygame.draw.polygon(window,black,((50,50),(100,50),(100,100),(50,100)),1)
  pygame.draw.line(window,black,(x11,y11),(x21,y21),1)   


cohen_sutherland_algo(80,120,120,30)
 
while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 pygame.display.update()
 clock.tick(100)
