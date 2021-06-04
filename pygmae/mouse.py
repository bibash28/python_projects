import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Mouse")
win.fill(white)
clock = pygame.time.Clock()

def message(message):
 font = pygame.font.Font('freesansbold.ttf',32)
 surface = font.render(message,True,black,white)
 win.blit(surface,(1,1))

rec = pygame.draw.rect(win, red, (100,100,200,50))

gameon = True
while gameon:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()

  if event.type == pygame.MOUSEMOTION:
   x,y = event.pos
   if rec.collidepoint((x,y)):
    message("Rectangle Touched")
  
  if event.type == pygame.MOUSEBUTTONUP: 
   x,y = event.pos
   if rec.collidepoint((x,y)):
    message("Clicked and released")

 pygame.display.update()
 clock.tick(100)


