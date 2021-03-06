import pygame
pygame.init()
from math import sin, cos, radians

window = pygame.display.set_mode((640,480))
pygame.display.set_caption("Homogeneous Transformation")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
brown = (244,164,96)
grey = (220,220,220)

window.fill(white)

def _3Dto2Dconverter(x,y,z):
 fov = 256
 viewer_distance = 4
 half_screen_width = 640 / 2
 half_screen_height = 480 / 2
 a = x * fov / (z + viewer_distance) + half_screen_width
 b = -y * fov / (z + viewer_distance) + half_screen_height
 return a,b


def translate(x,y,z,tx,ty,tz):
 A = [[1, 0, 0, tx],
      [0, 1, 0, ty],
      [0, 0, 1, tz],
      [0, 0, 0, 1]]

 B = [[x],
      [y],
      [z], 
      [1]]
 
 result = [[0],
           [0],
           [0],
           [1]]

 # iterate through rows of A
 for i in range(len(A)):
   # iterate through columns of B
   for j in range(len(B[0])):
       # iterate through rows of B
       for k in range(len(B)):
           result[i][j] += A[i][k] * B[k][j]

 return result[0][0],result[1][0],result[2][0]


'''
pygame.draw.polygon(window,black,((50,50),(20,100),(80,100)),1)
#translation
tx,ty = 100,100
a1,b1 = translate(50,50,tx,ty)
a2,b2 = translate(20,100,tx,ty)
a3,b3 = translate(80,100,tx,ty)
pygame.draw.polygon(window,red,((a1,b1),(a2,b2),(a3,b3)),1)
'''
#before
a1, b1, c1 = 2+0, 2+0, 2+0 
a2, b2, c2 = 2+1, 2+0, 2+0
a3, b3, c3 = 2+0, 2+1, 2+0
a4, b4, c4 = 2+1, 2+1, 2+0
a5, b5, c5 = 2+0, 2+0, 2+1
a6, b6, c6 = 2+1, 2+0, 2+1
a7, b7, c7 = 2+0, 2+1, 2+1
a8, b8, c8 = 2+1, 2+1, 2+1

x1, y1 = _3Dto2Dconverter(a1, b1, c1)
x2, y2 = _3Dto2Dconverter(a2, b2, c2)
x3, y3 = _3Dto2Dconverter(a3, b3, c3)
x4, y4 = _3Dto2Dconverter(a4, b4, c4)
x5, y5 = _3Dto2Dconverter(a5, b5, c5)
x6, y6 = _3Dto2Dconverter(a6, b6, c6)
x7, y7 = _3Dto2Dconverter(a7, b7, c7)
x8, y8 = _3Dto2Dconverter(a8, b8, c8)

pygame.draw.polygon(window,black,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(window,black,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(window,black,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(window,black,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)

#after
tx,ty,tz = 5, 5, 5
a1,b1,c1 = translate(a1,b1,c1,tx,ty,tz)
a2,b2,c2 = translate(a2,b2,c2,tx,ty,tz)
a3,b3,c3 = translate(a3,b3,c3,tx,ty,tz)
a4,b4,c4 = translate(a4,b4,c4,tx,ty,tz)
a5,b5,c5 = translate(a5,b5,c5,tx,ty,tz)
a6,b6,c6 = translate(a6,b6,c6,tx,ty,tz)
a7,b7,c7 = translate(a7,b7,c7,tx,ty,tz)
a8,b8,c8 = translate(a8,b8,c8,tx,ty,tz)

x1, y1 = _3Dto2Dconverter(a1, b1, c1)
x2, y2 = _3Dto2Dconverter(a2, b2, c2)
x3, y3 = _3Dto2Dconverter(a3, b3, c3)
x4, y4 = _3Dto2Dconverter(a4, b4, c4)
x5, y5 = _3Dto2Dconverter(a5, b5, c5)
x6, y6 = _3Dto2Dconverter(a6, b6, c6)
x7, y7 = _3Dto2Dconverter(a7, b7, c7)
x8, y8 = _3Dto2Dconverter(a8, b8, c8)

pygame.draw.polygon(window,red,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(window,red,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(window,red,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(window,red,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)


while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 


 pygame.display.update()
 clock.tick(100)
