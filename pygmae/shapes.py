import pygame

pygame.init()
win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes")
win.fill((255,255,255))
clock = pygame.time.Clock()

#pygame.draw.line(win, (0,255,0), (60,60),(120,120),4)
#pygame.draw.circle(win,(0,0,0),(333,300),55,2)
#pygame.draw.rect(win,(0,0,0),(200,150,100,50),0)
#x,y coordinate of top left,width,height
#pygame.draw.ellipse(win,(0,0,0),(300,250,40,80),2)
#boundingrectangle
#pygame.draw.polygon(win, (255,0,0),((146,0),(291,106),(236,277),(56,277),(0,106)))
#no width -> color is filled(0,0,0)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, (0,255,0),(0,0,255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

running = True
while running:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   running = False
 pygame.display.update()
 clock.tick(60)

pygame.quit()
quit()

