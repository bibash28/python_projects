import pygame
pygame.init()

white = (255,255,255)
black = (0,0,0)

win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Image Button")
win.fill(white)
clock = pygame.time.Clock()

button = pygame.image.load('car.png')
a = 150
b = 150
win.blit(button,(a,b))

def message(message):
 font = pygame.font.Font('freesansbold.ttf',32)
 surface = font.render(message,True,black,white)
 win.blit(surface,(200,500))
 
while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
 
  if event.type == pygame.MOUSEBUTTONUP:
   x,y = event.pos
   if button.get_rect(topleft = (a,b)).collidepoint((x,y)):
    message('  Image Clicked  ')
   else:
    message('Outside Clicked')
 
 pygame.display.update()
 clock.tick(200)












