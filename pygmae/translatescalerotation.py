import pygame
pygame.init()
from math import sin, cos, radians

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Homogeneous Transformation")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
brown = (244,164,96)
grey = (220,220,220)

window.fill(white)

def translate(x,y,tx,ty):
 A = [[1, 0, tx],
      [0, 1, ty],
      [0, 0, 1]]

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

def scaling(x,y,sx,sy):
 A = [[sx, 0, 0],
      [0, sy, 0],
      [0, 0, 1]]

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

def rotation(x,y,theta):
 A = [[cos(theta), -sin(theta), 0],
      [sin(theta), cos(theta), 0],
      [0,           0,         1]]

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

pygame.draw.polygon(window,black,((50,50),(20,100),(80,100)),1)
#translation
tx,ty = 100,100
a1,b1 = translate(50,50,tx,ty)
a2,b2 = translate(20,100,tx,ty)
a3,b3 = translate(80,100,tx,ty)
pygame.draw.polygon(window,red,((a1,b1),(a2,b2),(a3,b3)),1)

#scaling
sx,sy = 1.5,1.5
c1,d1 = scaling(50,50,sx,sy)
c2,d2 = scaling(20,100,sx,sy)
c3,d3 = scaling(80,100,sx,sy)
pygame.draw.polygon(window,blue,((c1,d1),(c2,d2),(c3,d3)),1)

#rotation
theta = radians(-40)
e1,f1 = rotation(50,50,theta)
e2,f2 = rotation(20,100,theta)
e3,f3 = rotation(80,100,theta)
pygame.draw.polygon(window,brown,((e1,f1),(e2,f2),(e3,f3)),1)

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 pygame.display.update()
 clock.tick(100)
