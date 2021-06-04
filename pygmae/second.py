import pygame

pygame.init()
win = pygame.display.set_mode((200,200))
pygame.display.set_caption('Second Program')
clock = pygame.time.Clock()

running = True
while running:
 for event in pygame.event.get(): #get event happening
  if event.type == pygame.QUIT:
   running = False
  print(event)

 pygame.display.update() #same as flip
 clock.tick(60)  #60 frames per second

pygame.quit() #uninititae pygame
quit() #quit program
