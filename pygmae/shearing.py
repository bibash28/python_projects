import pygame
pygame.init()

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Homogeneous Shearing")
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

window.fill(white)

def x_dir_shear(x,y,shx):
 A = [[1, shx, 0],
      [0, 1,   0],
      [0, 0,   1]]

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

def y_dir_shear(x,y,shy):
 A = [[1, 0, 0],
      [shy, 1,   0],
      [0, 0,   1]]

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
#x_direction_shear
shx = 0.5
a1,b1 = x_dir_shear(50,50,shx)
a2,b2 = x_dir_shear(20,100,shx)
a3,b3 = x_dir_shear(80,100,shx)
pygame.draw.polygon(window,red,((a1,b1),(a2,b2),(a3,b3)),1)

#y_direction_shear
shy = 1
c1,d1 = y_dir_shear(50,50,shy)
c2,d2 = y_dir_shear(20,100,shy)
c3,d3 = y_dir_shear(80,100,shy)
pygame.draw.polygon(window,blue,((c1,d1),(c2,d2),(c3,d3)),1)


while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 pygame.display.update()
 clock.tick(100)
