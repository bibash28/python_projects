import pygame
import time
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Background Music")
win.fill((255,255,255))
clock = pygame.time.Clock()

pygame.mixer.music.load("drum.wav")
pygame.mixer.music.play(-1,0.0)
# -1 means infinte and 0.0 means from that second

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
  if event.type == pygame.KEYUP:
   if event.key == pygame.K_s:
    pygame.mixer.music.stop()
   elif event.key == pygame.K_p:
    pygame.mixer.music.pause()
   elif event.key == pygame.K_u:
    pygame.mixer.music.unpause()

 pygame.display.update()
 clock.tick(200)
 








