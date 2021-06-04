import pygame
pygame.init()
import time

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Liang Barsky LDA")
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

window.fill(white)


#clipping window
xwmin,ywmin = 50, 50
xwmax,ywmax = 100, 100
pygame.draw.polygon(window,black,((50,50),(100,50),(100,100),(50,100)),1)  #(initialpoints, length)

x1, y1 = 80, 120
x2, y2 = 120, 50
pygame.draw.line(window,black,(x1,y1),(x2,y2),1)

dx = x2 - x1
dy = y2 - y1

P1 = -dx
P2 = dx
P3 = -dy
P4 = dy

q1 = x1 - xwmin
q2 = xwmax - x1
q3 = y1 - ywmin
q4 = ywmax - y1

r1 = q1/P1
r2 = q2/P2
r3 = q3/P3
r4 = q4/P4

a = []
b = []
if P1 < 0:
 a.append(r1)
else:
 b.append(r1)
if P2 < 0:
 a.append(r2)
else:
 b.append(r2)
if P3 < 0:
 a.append(r3)
else:
 b.append(r3)
if P4 < 0:
 a.append(r4)
else:
 b.append(r4)

u1 = max(0, max(a))
u2 = min(1, min(b))

if u1 > u2:
 #completely outside
 pass
else:
 x11 = x1 + (u1*dx)
 y11 = y1 + (u1*dy)
 x21 = x1 + (u2*dx)
 y21 = y1 + (u2*dy)

pygame.display.update()
time.sleep(1)  
window.fill(white) 
pygame.draw.polygon(window,black,((50,50),(100,50),(100,100),(50,100)),1)
pygame.draw.line(window,black,(x11,y11),(x21,y21),1)   


 
while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 pygame.display.update()
 clock.tick(100)
