import pygame

pygame.init()

def goat_second_click(g1_x,g1_y,left_for_goat):
     second_click = True
     while second_click:
        for event in pygame.event.get(): 
         if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == K_ESCAPE):
           end_attempt()

         if event.type == pygame.MOUSEBUTTONUP:
          if b1.get_rect(topleft = (a1_x,a1_y)).collidepoint((event.pos)):
           if 'a1' in left_for_goat:
            g1_x,g1_y = a1_x,a1_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 
            
          elif b2.get_rect(topleft = (a2_x,a2_y)).collidepoint((event.pos)):
           if 'a2' in left_for_goat:
            g1_x,g1_y = a2_x,a2_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y
            
          elif b3.get_rect(topleft = (a3_x,a3_y)).collidepoint((event.pos)):
           if 'a3' in left_for_goat:
            g1_x,g1_y = a3_x,a3_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y
                  
          elif b4.get_rect(topleft = (a4_x,a4_y)).collidepoint((event.pos)):
           if 'a4' in left_for_goat:
            g1_x,g1_y = a4_x,a4_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y
            
          elif b5.get_rect(topleft = (a5_x,a5_y)).collidepoint((event.pos)):
           if 'a5' in left_for_goat:
            g1_x,g1_y = a5_x,a5_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y            
            
          elif b6.get_rect(topleft = (b1_x,b1_y)).collidepoint((event.pos)):
           if 'b1' in left_for_goat:
            g1_x,g1_y = b1_x,b1_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b7.get_rect(topleft = (b2_x,b2_y)).collidepoint((event.pos)):
           if 'b2' in left_for_goat:
            g1_x,g1_y = b2_x,b2_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b8.get_rect(topleft = (b3_x,b3_y)).collidepoint((event.pos)):
           if 'b3' in left_for_goat:
            g1_x,g1_y = b3_x,b3_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y   
      
          elif b9.get_rect(topleft = (b4_x,b4_y)).collidepoint((event.pos)):
           if 'b4' in left_for_goat:
            g1_x,g1_y = b4_x,b4_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b10.get_rect(topleft = (b5_x,b5_y)).collidepoint((event.pos)):
           if 'b5' in left_for_goat:
            g1_x,g1_y = b5_x,b5_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y    
  
          elif b11.get_rect(topleft = (c1_x,c1_y)).collidepoint((event.pos)):
           if 'c1' in left_for_goat:
            g1_x,g1_y = c1_x,c1_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b2.get_rect(topleft = (c2_x,c2_y)).collidepoint((event.pos)):
           if 'c2' in left_for_goat:
            g1_x,g1_y = c2_x,c2_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b13.get_rect(topleft = (c3_x,c3_y)).collidepoint((event.pos)):
           if 'c3' in left_for_goat:
            g1_x,g1_y = c3_x,c3_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b14.get_rect(topleft = (c4_x,c4_y)).collidepoint((event.pos)):
           if 'c4' in left_for_goat:
            g1_x,g1_y = c4_x,c4_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b15.get_rect(topleft = (c5_x,c5_y)).collidepoint((event.pos)):
           if 'c5' in left_for_goat:
            g1_x,g1_y = c5_x,c5_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y   
     
          elif b16.get_rect(topleft = (d1_x,d1_y)).collidepoint((event.pos)):
           if 'd1' in left_for_goat:
            g1_x,g1_y = d1_x,d1_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b17.get_rect(topleft = (d2_x,d2_y)).collidepoint((event.pos)):
           if 'd2' in left_for_goat:
            g1_x,g1_y = d2_x,d2_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b8.get_rect(topleft = (d3_x,d3_y)).collidepoint((event.pos)):
           if 'd3' in left_for_goat:
            g1_x,g1_y = d3_x,d3_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y      
  
          elif b19.get_rect(topleft = (d4_x,d4_y)).collidepoint((event.pos)):
           if 'd4' in left_for_goat:
            g1_x,g1_y = d4_x,d4_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b20.get_rect(topleft = (d5_x,d5_y)).collidepoint((event.pos)):
           if 'd5' in left_for_goat:
            g1_x,g1_y = d5_x,d5_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b21.get_rect(topleft = (e1_x,e1_y)).collidepoint((event.pos)):
           if 'e1' in left_for_goat:
            g1_x,g1_y = e1_x,e1_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b22.get_rect(topleft = (e2_x,e2_y)).collidepoint((event.pos)):
           if 'e2' in left_for_goat:
            g1_x,g1_y = e2_x,e2_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b23.get_rect(topleft = (e3_x,e3_y)).collidepoint((event.pos)):
           if 'e3' in left_for_goat:
            g1_x,g1_y = e3_x,e3_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y     
  
          elif b24.get_rect(topleft = (e4_x,e4_y)).collidepoint((event.pos)):
           if 'e4' in left_for_goat:
            g1_x,g1_y = e4_x,e4_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b25.get_rect(topleft = (e5_x,e5_y)).collidepoint((event.pos)):
           if 'e5' in left_for_goat:
            g1_x,g1_y = e5_x,e5_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          else:
           return g1_x,g1_y





def goat_second_click_20plus(g1_x,g1_y,goat_possible_moves):
     second_click = True
     while second_click:
        for event in pygame.event.get(): 
         if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == K_ESCAPE):
           end_attempt()

         if event.type == pygame.MOUSEBUTTONUP:
          if b1.get_rect(topleft = (a1_x,a1_y)).collidepoint((event.pos)):
           if 'a1' in goat_possible_moves:
            g1_x,g1_y = a1_x,a1_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 
            
          elif b2.get_rect(topleft = (a2_x,a2_y)).collidepoint((event.pos)):
           if 'a2' in goat_possible_moves:
            g1_x,g1_y = a2_x,a2_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y
            
          elif b3.get_rect(topleft = (a3_x,a3_y)).collidepoint((event.pos)):
           if 'a3' in goat_possible_moves:
            g1_x,g1_y = a3_x,a3_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y
                  
          elif b4.get_rect(topleft = (a4_x,a4_y)).collidepoint((event.pos)):
           if 'a4' in goat_possible_moves:
            g1_x,g1_y = a4_x,a4_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y
            
          elif b5.get_rect(topleft = (a5_x,a5_y)).collidepoint((event.pos)):
           if 'a5' in goat_possible_moves:
            g1_x,g1_y = a5_x,a5_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y            
            
          elif b6.get_rect(topleft = (b1_x,b1_y)).collidepoint((event.pos)):
           if 'b1' in goat_possible_moves:
            g1_x,g1_y = b1_x,b1_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b7.get_rect(topleft = (b2_x,b2_y)).collidepoint((event.pos)):
           if 'b2' in goat_possible_moves:
            g1_x,g1_y = b2_x,b2_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b8.get_rect(topleft = (b3_x,b3_y)).collidepoint((event.pos)):
           if 'b3' in goat_possible_moves:
            g1_x,g1_y = b3_x,b3_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y   
      
          elif b9.get_rect(topleft = (b4_x,b4_y)).collidepoint((event.pos)):
           if 'b4' in goat_possible_moves:
            g1_x,g1_y = b4_x,b4_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b10.get_rect(topleft = (b5_x,b5_y)).collidepoint((event.pos)):
           if 'b5' in goat_possible_moves:
            g1_x,g1_y = b5_x,b5_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y    
  
          elif b11.get_rect(topleft = (c1_x,c1_y)).collidepoint((event.pos)):
           if 'c1' in goat_possible_moves:
            g1_x,g1_y = c1_x,c1_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b2.get_rect(topleft = (c2_x,c2_y)).collidepoint((event.pos)):
           if 'c2' in goat_possible_moves:
            g1_x,g1_y = c2_x,c2_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b13.get_rect(topleft = (c3_x,c3_y)).collidepoint((event.pos)):
           if 'c3' in goat_possible_moves:
            g1_x,g1_y = c3_x,c3_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b14.get_rect(topleft = (c4_x,c4_y)).collidepoint((event.pos)):
           if 'c4' in goat_possible_moves:
            g1_x,g1_y = c4_x,c4_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b15.get_rect(topleft = (c5_x,c5_y)).collidepoint((event.pos)):
           if 'c5' in goat_possible_moves:
            g1_x,g1_y = c5_x,c5_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y   
     
          elif b16.get_rect(topleft = (d1_x,d1_y)).collidepoint((event.pos)):
           if 'd1' in goat_possible_moves:
            g1_x,g1_y = d1_x,d1_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b17.get_rect(topleft = (d2_x,d2_y)).collidepoint((event.pos)):
           if 'd2' in goat_possible_moves:
            g1_x,g1_y = d2_x,d2_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b8.get_rect(topleft = (d3_x,d3_y)).collidepoint((event.pos)):
           if 'd3' in goat_possible_moves:
            g1_x,g1_y = d3_x,d3_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y      
  
          elif b19.get_rect(topleft = (d4_x,d4_y)).collidepoint((event.pos)):
           if 'd4' in goat_possible_moves:
            g1_x,g1_y = d4_x,d4_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b20.get_rect(topleft = (d5_x,d5_y)).collidepoint((event.pos)):
           if 'd5' in goat_possible_moves:
            g1_x,g1_y = d5_x,d5_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b21.get_rect(topleft = (e1_x,e1_y)).collidepoint((event.pos)):
           if 'e1' in goat_possible_moves:
            g1_x,g1_y = e1_x,e1_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b22.get_rect(topleft = (e2_x,e2_y)).collidepoint((event.pos)):
           if 'e2' in goat_possible_moves:
            g1_x,g1_y = e2_x,e2_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b23.get_rect(topleft = (e3_x,e3_y)).collidepoint((event.pos)):
           if 'e3' in goat_possible_moves:
            g1_x,g1_y = e3_x,e3_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y     
  
          elif b24.get_rect(topleft = (e4_x,e4_y)).collidepoint((event.pos)):
           if 'e4' in goat_possible_moves:
            g1_x,g1_y = e4_x,e4_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          elif b25.get_rect(topleft = (e5_x,e5_y)).collidepoint((event.pos)):
           if 'e5' in goat_possible_moves:
            g1_x,g1_y = e5_x,e5_y
            return g1_x,g1_y
           else:
            return g1_x,g1_y 

          else:
           return g1_x,g1_y



#board places
a1_x, b1_x, c1_x, d1_x, e1_x = 234, 234, 234, 234, 234
a1_y, b1_y, c1_y, d1_y, e1_y = 620, 479, 315, 162, 11
a2_x, b2_x, c2_x, d2_x, e2_x = 392, 392, 392, 392, 392
a2_y, b2_y, c2_y, d2_y, e2_y = 620, 479, 315, 162, 11
a3_x, b3_x, c3_x, d3_x, e3_x = 549, 549, 549, 549, 549
a3_y, b3_y, c3_y, d3_y, e3_y = 620, 479, 315, 162, 11
a4_x, b4_x, c4_x, d4_x, e4_x = 707, 707, 707, 707, 707
a4_y, b4_y, c4_y, d4_y, e4_y = 620, 479, 315, 162, 11
a5_x, b5_x, c5_x, d5_x, e5_x = 865, 865, 865, 865, 865
a5_y, b5_y, c5_y, d5_y, e5_y = 620, 479, 315, 162, 11

#25 surfaces
b1 = pygame.image.load("blank.png")
b2 = pygame.image.load("blank.png")
b3 = pygame.image.load("blank.png")
b4 = pygame.image.load("blank.png")
b5 = pygame.image.load("blank.png")
b6 = pygame.image.load("blank.png")
b7 = pygame.image.load("blank.png")
b8 = pygame.image.load("blank.png")
b9 = pygame.image.load("blank.png")
b10 = pygame.image.load("blank.png")
b11 = pygame.image.load("blank.png")
b12 = pygame.image.load("blank.png")
b13 = pygame.image.load("blank.png")
b14 = pygame.image.load("blank.png")
b15 = pygame.image.load("blank.png")
b16 = pygame.image.load("blank.png")
b17 = pygame.image.load("blank.png")
b18 = pygame.image.load("blank.png")
b19 = pygame.image.load("blank.png")
b20 = pygame.image.load("blank.png")
b21 = pygame.image.load("blank.png")
b22 = pygame.image.load("blank.png")
b23 = pygame.image.load("blank.png")
b24 = pygame.image.load("blank.png")
b25 = pygame.image.load("blank.png")

