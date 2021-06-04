import pygame

pygame.init()

window = pygame.display.set_mode((400,300))
pygame.display.set_caption("Text Print")
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
window.fill(white)


def message(text):
 fontObj = pygame.font.Font('freesansbold.ttf',32) #name,size
 textSurfaceObj = fontObj.render(text,True, black, green) 
 textRectObj = textSurfaceObj.get_rect()
 textRectObj.center = (200, 150)
 window.blit(textSurfaceObj, textRectObj)


while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   quit()
  if event.type == pygame.KEYDOWN: #keydown -> push key
   if event.key == pygame.K_UP:
    message('Pressed Up')
   elif event.key == pygame.K_DOWN:
    message('Pressed Down')
   elif event.key == pygame.K_LEFT:
    message('Pressed Left')
   elif event.key == pygame.K_RIGHT:
    message('Pressed Right')
 

 pygame.display.update()
 clock.tick(60)










 
