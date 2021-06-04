import pygame
from math import sin, cos, radians, pi
import time
pygame.init(), 

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("House")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
blue = (135, 206, 235)
grey = (220,220,220)

window.fill(grey)
pygame.draw.polygon(window,white,((175,380),(225,380),(200,175)))

def rotation(x,y,xr,yr,theta):
 A = [[cos(theta), -sin(theta), (xr*(1 - cos(theta))) + (yr*(sin(theta)))],
      [sin(theta), cos(theta),  (yr*(1 - cos(theta))) - (xr*(sin(theta)))],
      [0,              0,                    1                           ]]

 B = [[x],
      [y],
      [1]]

 result = [[0],
           [0],
           [0]]

 # iterate through rows of A
 for i in range(len(A)):
   # iterate through columns of B
   for j in range(len(B[0])):
       # iterate through rows of B
       for k in range(len(B)):
           result[i][j] += A[i][k] * B[k][j]
 
 return result[0][0],result[1][0]

a1,b1,a2,b2 = 215, 100, 280, 140
c1,d1,c2,d2 = 270, 220, 220, 265
e1,f1,e2,f2 = 130, 230, 115, 175
pygame.draw.polygon(window,blue,((200,175),(a1,b1),(a2,b2)))
pygame.draw.polygon(window,blue,((200,175),(c1,d1),(c2,d2)))
pygame.draw.polygon(window,blue,((200,175),(e1,f1),(e2,f2)))

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()

 theta = radians(1)
 a1,b1 = rotation(a1,b1,200,175,theta)
 a2,b2 = rotation(a2,b2,200,175,theta)
 c1,d1 = rotation(c1,d1,200,175,theta)
 c2,d2 = rotation(c2,d2,200,175,theta)
 e1,f1 = rotation(e1,f1,200,175,theta)
 e2,f2 = rotation(e2,f2,200,175,theta)

 pygame.display.update()
 window.fill(grey)
 pygame.draw.polygon(window,white,((175,380),(225,380),(200,175)))
 pygame.draw.polygon(window,blue,((200,175),(a1,b1),(a2,b2)))
 pygame.draw.polygon(window,blue,((200,175),(c1,d1),(c2,d2)))
 pygame.draw.polygon(window,blue,((200,175),(e1,f1),(e2,f2)))
 pygame.display.update()
 clock.tick(500000)

