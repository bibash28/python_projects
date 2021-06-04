import pygame
pygame.init()

window = pygame.display.set_mode((250,200))
pygame.display.set_caption("Resolution")
clock = pygame.time.Clock()

window.fill((255,255,255))

surface = pygame.display.get_surface()
print("Width: "+str(surface.get_width()))
print("Height: "+str(surface.get_height()))



while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()

 pygame.display.update()
 clock.tick(20)
