import pygame
pygame.init()
import time

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Polygon Clipping LDA")
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

window.fill(white)

def left_clipper(x1, y1, x2, y2):
 if x2 - x1 != 0:
  m = (y2 - y1)/(x2 - x1)
 else:
  m = 10000
 if (x1 > xwmin) and (x2 > xwmin): #wholly inside
  x1 = x1
  y1 = y1
  x2 = x2
  y2 = y2
 elif (x1 < xwmin) and (x2 > xwmin): #outside inside
  x1 = xwmin
  y1 = y2 - (m*(x2 - x1))
  x2 = x2
  y2 = y2
 elif (x1 < xwmin) and (x2 < xwmin): #wholly outside
  pass
 elif (x1 > xwmin) and (x2 < xwmin): #inside outside
  x1 = x1
  y1 = y1
  x2 = xwmin
  y2 = y1 + (m*(x2 - x1))
 return x1, y1, x2, y2


def top_clipper(x1, y1, x2, y2):
 if x2 - x1 != 0:
  m = (y2 - y1)/(x2 - x1)
 else:
  m = 10000
 if (y1 > ywmin) and (y2 > ywmin): #wholly inside
  x1 = x1
  y1 = y1
  x2 = x2
  y2 = y2
 elif (y1 < ywmin) and (y2 > ywmin): #outside inside
  y1 = ywmin
  x1 = x2 - ((y2 - y1)/m)
  x2 = x2
  y2 = y2
 elif (y1 < ywmin) and (y2 < ywmin): #wholly outside
  pass
 elif (y1 > ywmin) and (y2 < ywmin): #inside outside
  x1 = x1
  y1 = y1
  y2 = ywmin
  x2 = x1 + ((y2 - y1)/m)
 return x1, y1, x2, y2


def right_clipper(x1, y1, x2, y2):
 if x2 - x1 != 0:
  m = (y2 - y1)/(x2 - x1)
 else:
  m = 10000
 if (x1 < xwmax) and (x2 < xwmax): #wholly inside
  x1 = x1
  y1 = y1
  x2 = x2
  y2 = y2
 elif (x1 > xwmax) and (x2 < xwmax): #outside inside
  x1 = xwmax
  y1 = y2 - (m*(x2 - x1))
  x2 = x2
  y2 = y2
 elif (x1 > xwmax) and (x2 > xwmax): #wholly outside
  pass
 elif (x1 < xwmax) and (x2 > xwmax): #inside outside
  x1 = x1
  y1 = y1
  x2 = xwmax
  y2 = y1 + (m*(x2 - x1))
 return x1, y1, x2, y2


def bottom_clipper(x1, y1, x2, y2):
 if x2 - x1 != 0:
  m = (y2 - y1)/(x2 - x1)
 else:
  m = 10000
 if (y1 < ywmax) and (y2 < ywmax): #wholly inside
  x1 = x1
  y1 = y1
  x2 = x2
  y2 = y2
 elif (y1 > ywmax) and (y2 < ywmax): #outside inside
  y1 = ywmax
  x1 = x2 - ((y2 - y1)/m)
  x2 = x2
  y2 = y2
 elif (y1 > ywmax) and (y2 > ywmax): #wholly outside
  pass
 elif (y1 < ywmax) and (y2 > ywmax): #inside outside
  x1 = x1
  y1 = y1
  y2 = ywmax
  x2 = x1 + ((y2 - y1)/m)
 return x1, y1, x2, y2


#clipping window
xwmin,ywmin = 10, 10
xwmax,ywmax = 80, 80
pygame.draw.polygon(window,black,((10,10),(10,80),(80,80),(80,10)),1)  #(initialpoints, length)

#polygon
x1, y1, x2, y2, x3, y3 = 5, 40, 50, 85, 50, 5
x11, y11, x21, y21, x31, y31 = 5, 40, 50, 85, 50, 5
pygame.draw.line(window,black,(x1,y1),(x2,y2),1)
pygame.draw.line(window,black,(x21,y21),(x3,y3),1)
pygame.draw.line(window,black,(x31,y31),(x11,y11),1)
 
#left_clipper
x1, y1, x2, y2 = left_clipper(x1, y1, x2, y2)
x21, y21, x3, y3 = left_clipper(x21, y21, x3, y3)
x31, y31, x11, y11 = left_clipper(x31, y31, x11, y11)
pygame.display.update()
time.sleep(1)
window.fill(white)
pygame.draw.polygon(window,black,((10,10),(10,80),(80,80),(80,10)),1)
pygame.draw.line(window,black,(x1,y1),(x2,y2),1)
pygame.draw.line(window,black,(x21,y21),(x3,y3),1)
pygame.draw.line(window,black,(x31,y31),(x11,y11),1)

#top_clipper(bottom clipper in copy)
x1, y1, x2, y2 = top_clipper(x1, y1, x2, y2)
x21, y21, x3, y3 = top_clipper(x21, y21, x3, y3)
x31, y31, x11, y11 = top_clipper(x31, y31, x11, y11)
pygame.display.update()
time.sleep(1)
window.fill(white)
pygame.draw.polygon(window,black,((10,10),(10,80),(80,80),(80,10)),1)
pygame.draw.line(window,black,(x1,y1),(x2,y2),1)
pygame.draw.line(window,black,(x21,y21),(x3,y3),1)
pygame.draw.line(window,black,(x31,y31),(x11,y11),1)

#right_clipper
x1, y1, x2, y2 = right_clipper(x1, y1, x2, y2)
x21, y21, x3, y3 = right_clipper(x21, y21, x3, y3)
x31, y31, x11, y11 = right_clipper(x31, y31, x11, y11)
pygame.display.update()
time.sleep(1)
window.fill(white)
pygame.draw.polygon(window,black,((10,10),(10,80),(80,80),(80,10)),1)
pygame.draw.line(window,black,(x1,y1),(x2,y2),1)
pygame.draw.line(window,black,(x21,y21),(x3,y3),1)
pygame.draw.line(window,black,(x31,y31),(x11,y11),1)

#bottom_clipper(top clipper in copy)
x1, y1, x2, y2 = bottom_clipper(x1, y1, x2, y2)
x21, y21, x3, y3 = bottom_clipper(x21, y21, x3, y3)
x31, y31, x11, y11 = bottom_clipper(x31, y31, x11, y11)
pygame.display.update()
time.sleep(1)
window.fill(white)
pygame.draw.polygon(window,black,((10,10),(10,80),(80,80),(80,10)),1)
pygame.draw.line(window,black,(x1,y1),(x2,y2),1)
pygame.draw.line(window,black,(x21,y21),(x3,y3),1)
pygame.draw.line(window,black,(x31,y31),(x11,y11),1)


while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 pygame.display.update()
 clock.tick(100)
