import pygame
import time

pygame.init()

window = pygame.display.set_mode((200,200))
pygame.display.set_caption("Sound play")
clock = pygame.time.Clock()

soundObj = pygame.mixer.Sound("crash.wav")

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
  if event.type == pygame.MOUSEBUTTONDOWN:
   soundObj.play()
   time.sleep(1) #wait 1 second and play
   soundObj.stop()
  
 
 pygame.display.update()
 clock.tick(60)



 
