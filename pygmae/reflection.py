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

def reflection_x(x,y):
 A = [[1, 0, 0],
      [0,-1, 0],
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


def reflection_y(x,y):
 A = [[-1, 0, 0],
       [0, 1, 0],
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

#x-axis
pygame.draw.line(window,black,(0,200),(400,200),1)
#y-axis
pygame.draw.line(window,black,(200,0),(200,400),1)

#origin is (200,200)
#triangle
pygame.draw.polygon(window,black,((300,50),(250,100),(350,100)),1)

#relection on x axis
a1,b1 = reflection_x(300,50)
a2,b2 = reflection_x(250,100)
a3,b3 = reflection_x(350,100)
pygame.draw.polygon(window,red,((a1,400+b1),(a2,400+b2),(a3,400+b3)),1)

#relection on y axis
c1,d1 = reflection_y(300,50)
c2,d2 = reflection_y(250,100)
c3,d3 = reflection_y(350,100)
print(c1,d1,c2,d2,c3,d3)
pygame.draw.polygon(window,blue,((400+c1,d1),(400+c2,d2),(400+c3,d3)),1)


while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 pygame.display.update()
 clock.tick(100)
