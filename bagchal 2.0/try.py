import pygame
 
pygame.init()
width=1000
height=1000
screen = pygame.display.set_mode( (width, height ) )
pygame.display.set_caption('clicked on image')
r = pygame.image.load("tiger.png")

 
x = 918; # x coordnate of image
y = 920; # y coordinate of image
screen.blit(r ,  ( x,y)) # paint to screen
#pygame.display.flip() # paint screen one time
 
running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if r.get_rect(center = (918,920)).collidepoint((x, y)):
                print('clicked on image')
    pygame.display.update()
#loop over, quite pygame
pygame.quit()
