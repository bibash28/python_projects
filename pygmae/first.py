ximport pygame

win = pygame.display.set_mode((300,400))
pygame.display.set_caption("First one")
win.fill((255,255,255))

pygame.display.flip()  #indicates end of the program

running = True
while running:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   running = False

