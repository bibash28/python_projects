import pygame
pygame.init()

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("House")
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
brown = (244,164,96)
grey = (220,220,220)

window.fill(grey)

#triangle_topleft
pygame.draw.polygon(window,black,((60,30),(20,70),(100,70)),2)
#parm_topright
pygame.draw.polygon(window,white,((60,30),(100,70),(360,70),(320,30)),0)
pygame.draw.polygon(window,black,((60,30),(100,70),(360,70),(320,30)),2)

pygame.draw.rect(window,red,(20,70,80,130),0)
pygame.draw.rect(window,black,(20,70,80,130),2)

pygame.draw.rect(window,grey,(50,135,20,65),0)
pygame.draw.rect(window,black,(50,135,20,65),2)

pygame.draw.rect(window,blue,(100,70,260,130),0)
pygame.draw.rect(window,black,(100,70,260,130),2)

for i in range(1,160,40):
 pygame.draw.rect(window,brown,(150+i,110,40,50),0) 
 pygame.draw.rect(window,black,(150+i,110,40,50),2) 
 
pygame.draw.line(window,black,(150,135),(310,135),2)

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 pygame.display.update()
 clock.tick(70)
