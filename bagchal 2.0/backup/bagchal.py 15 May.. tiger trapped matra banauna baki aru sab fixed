import pygame
import time
from position import board_pos
from movetypes import poss_moves
from goatmovement import goat_second_click_20plus, goat_second_click
from tigermovement import tiger_second_click
from tigerjump import tiger_newmove
from boardtoanimalconverter import get_animal_coordinate #, get_animal

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("BagChal")
clock = pygame.time.Clock()

#change upon the user's choice
goat_turns = True
tiger_turns = False

#space occupied by goat and tiger at first
goat_space_occupied = []
#goat_space_occupied = ["b1","b3","b5"] #temporaary
tiger_space_occupied = ['a1','a5','e1','e5']
total_place = ['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5']

#temporary goat place
temp_goat_place = []

moved_out_goat_count = 0
tiger_trapped_count = 0
goat_move_switch = 1


#board places
#global a1_x, b1_x, c1_x, d1_x, e1_x, a1_y, b1_y, c1_y, d1_y, e1_y
#global a2_x, b2_x, c2_x, d2_x, e2_x, a2_y, b2_y, c2_y, d2_y, e2_y  
#global a3_x, b3_x, c3_x, d3_x, e3_x, a3_y, b3_y, c3_y, d3_y, e3_y  
#global a4_x, b4_x, c4_x, d4_x, e4_x, a4_y, b4_y, c4_y, d4_y, e4_y  
#global a5_x, b5_x, c5_x, d5_x, e5_x, a5_y, b5_y, c5_y, d5_y, e5_y  
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

#16goat
#global g1_x, g2_x, g3_x, g4_x, g5_x, g6_x, g7_x, g8_x, g9_x, g10_, g1_y, g2_y, g3_y, g4_y, g5_y, g6_y, g7_y, g8_y, g9_y, g10_y
#global g11_x, g12_x, g13_x, g14_x, g15_x, g16_x, g17_x, g18_x, g19_x, g20_x, g11_y, g12_y, g13_y, g14_y, g15_y, g16_y, g17_y, g18_y, g19_y, g20_y 
'''
#temporary
g1_x, g2_x, g3_x, g4_x, g5_x, g6_x, g7_x, g8_x, g9_x, g10_x = 234, 549, 865,  77,  77,  77,  77,  77,  77,  77
g1_y, g2_y, g3_y, g4_y, g5_y, g6_y, g7_y, g8_y, g9_y, g10_y = 479, 479, 479, 237, 313, 389, 465, 540, 616, 693
'''
g1_x, g2_x, g3_x, g4_x, g5_x, g6_x, g7_x, g8_x, g9_x, g10_x = 77, 77, 77,  77,  77,  77,  77,  77,  77,  77
g1_y, g2_y, g3_y, g4_y, g5_y, g6_y, g7_y, g8_y, g9_y, g10_y =  8, 84, 161, 237, 313, 389, 465, 540, 616, 693

g11_x, g12_x, g13_x, g14_x, g15_x, g16_x, g17_x, g18_x, g19_x, g20_x = 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020 
g11_y, g12_y, g13_y, g14_y, g15_y, g16_y, g17_y, g18_y, g19_y, g20_y = 10,   86,   163,  239,  315,  391,  467,  542,  618,  695

g1 = pygame.image.load("goat.png")
g2 = pygame.image.load("goat.png")
g3 = pygame.image.load("goat.png")
g4 = pygame.image.load("goat.png")
g5 = pygame.image.load("goat.png")
g6 = pygame.image.load("goat.png")
g7 = pygame.image.load("goat.png")
g8 = pygame.image.load("goat.png")
g9 = pygame.image.load("goat.png")
g10 = pygame.image.load("goat.png")
g11 = pygame.image.load("goat.png")
g12 = pygame.image.load("goat.png")
g13 = pygame.image.load("goat.png")
g14 = pygame.image.load("goat.png")
g15 = pygame.image.load("goat.png")
g16 = pygame.image.load("goat.png")
g17 = pygame.image.load("goat.png")
g18 = pygame.image.load("goat.png")
g19 = pygame.image.load("goat.png")
g20 = pygame.image.load("goat.png")

#4tigers
t1_x, t1_y = 234, 11
t2_x, t2_y = 234, 620
t3_x, t3_y = 865, 620
t4_x, t4_y = 865, 11

t1 = pygame.image.load("tiger.png")
t2 = pygame.image.load("tiger.png")
t3 = pygame.image.load("tiger.png")
t4 = pygame.image.load("tiger.png")

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


def message(text):
  font = pygame.font.Font('freesansbold.ttf',60)
  texts = font.render(text,True,black,white)
  win.blit(texts, (500,700))

def goat_turn():
 global goat_turns, tiger_turns    
 goat_turns = True
 tiger_turns = False

def tiger_turn():
 global goat_turns, tiger_turns    
 goat_turns = False
 tiger_turns = True
  
def end_attempt():
 pygame.quit()
 quit() 


def get_animal(x,y):
 global g1_x, g2_x, g3_x, g4_x, g5_x, g6_x, g7_x, g8_x, g9_x, g10_, g1_y, g2_y, g3_y, g4_y, g5_y, g6_y, g7_y, g8_y, g9_y, g10_y
 global g11_x, g12_x, g13_x, g14_x, g15_x, g16_x, g17_x, g18_x, g19_x, g20_x, g11_y, g12_y, g13_y, g14_y, g15_y, g16_y, g17_y, g18_y, g19_y, g20_y 
 global t1_x, t1_y, t2_x, t2_y, t3_x, t3_y, t4_x, t4_y

 if x == g1_x and y == g1_y :
  return 'g1'
 elif x == g2_x and y == g2_y:
  return 'g2'
 elif x == g3_x and y == g3_y:
  return 'g3'
 elif x == g4_x and y == g4_y:
  return 'g4'
 elif x == g5_x and y == g5_y:
  return 'g5'
 elif x == g6_x and y == g6_y:
  return 'g6'
 elif x == g7_x and y == g7_y:
  return 'g7'
 elif x == g8_x and y == g8_y:
  return 'g8'
 elif x == g9_x and y == g9_y:
  return 'g9'
 elif x == g10_x and y == g10_y:
  return 'g10'
 elif x == g11_x and y == g11_y:
  return 'g11'
 elif x == g12_x and y == g12_y:
  return 'g12'
 elif x == g13_x and y == g13_y:
  return 'g13'
 elif x == g14_x and y == g14_y:
  return 'g14'
 elif x == g15_x and y == g15_y:
  return 'g15'
 elif x == g16_x and y == g16_y:
  return 'g16'
 elif x == g17_x and y == g17_y:
  return 'g17'
 elif x == g18_x and y == g18_y:
  return 'g18'
 elif x == g19_x and y == g19_y:
  return 'g19'
 elif x == g20_x and y == g20_y:
  return 'g20'
 elif x == t1_x and y == t1_y:
  return 't1'
 elif x == t2_x and y == t2_y:
  return 't2'
 elif x == t3_x and y == t3_y:
  return 't3'
 elif x == t4_x and y == t4_y:
  return 't4'

def move_out_goat_sub(a,b,i):
  x1, y1 = 27,8
  x2, y2 = 27,693
  x3, y3 = 1070,10
  x4, y4 = 1070,693

  if i == 1:
   return x1, y1
  elif i == 2:
   return x2, y2
  elif i == 3:
   return x3, y3
  elif i == 4:
   return x4, y4
  elif i == 5:
   return a,b


def move_out_goat():
 global g1, g2, g3, g4, g5, g6, g7, g8, g9, g10_, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10
 global g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20 
 global g1_x, g2_x, g3_x, g4_x, g5_x, g6_x, g7_x, g8_x, g9_x, g10_x, g1_y, g2_y, g3_y, g4_y, g5_y, g6_y, g7_y, g8_y, g9_y, g10_y
 global g11_x, g12_x, g13_x, g14_x, g15_x, g16_x, g17_x, g18_x, g19_x, g20_x, g11_y, g12_y, g13_y, g14_y, g15_y, g16_y, g17_y, g18_y, g19_y, g20_y 
 global moved_out_goat_count 
 moved_out_goat_count+=1

 if out_goat == 'g1':
  g1 = pygame.image.load("goat_out.png")
  g1_x,g1_y = move_out_goat_sub(g1_x,g1_y,moved_out_goat_count) 
   
 elif out_goat == 'g2':
  g2 = pygame.image.load("goat_out.png") 
  g2_x,g2_y = move_out_goat_sub(g2_x,g2_y,moved_out_goat_count)

 elif out_goat == 'g3':
  g3 = pygame.image.load("goat_out.png") 
  g3_x,g3_y = move_out_goat_sub(g3_x,g3_y,moved_out_goat_count)

 elif out_goat == 'g4':
  g4 = pygame.image.load("goat_out.png") 
  g4_x,g4_y = move_out_goat_sub(g4_x,g4_y,moved_out_goat_count) 

 elif out_goat == 'g5':
  g5 = pygame.image.load("goat_out.png") 
  g5_x,g5_y = move_out_goat_sub(g5_x,g5_y,moved_out_goat_count) 

 elif out_goat == 'g6':
  g6 = pygame.image.load("goat_out.png") 
  g6_x,g6_y = move_out_goat_sub(g6_x,g6_y,moved_out_goat_count)

 elif out_goat == 'g7':
  g7 = pygame.image.load("goat_out.png") 
  g7_x,g7_y = move_out_goat_sub(g7_x,g7_y,moved_out_goat_count)

 elif out_goat == 'g8':
  g8 = pygame.image.load("goat_out.png") 
  g8_x,g8_y = move_out_goat_sub(g8_x,g8_y,moved_out_goat_count)

 elif out_goat == 'g9':
  g9 = pygame.image.load("goat_out.png") 
  g9_x,g9_y = move_out_goat_sub(g9_x,g9_y,moved_out_goat_count)

 elif out_goat == 'g10':
  g10 = pygame.image.load("goat_out.png") 
  g10_x,g10_y = move_out_goat_sub(g10_x,g10_y,moved_out_goat_count) 

 elif out_goat == 'g11':
  g11 = pygame.image.load("goat_out.png")
  g11_x,g11_y = move_out_goat_sub(g11_x,g11_y,moved_out_goat_count)
   
 elif out_goat == 'g12':
  g12 = pygame.image.load("goat_out.png")
  g12_x,g12_y = move_out_goat_sub(g12_x,g12_y,moved_out_goat_count)

 elif out_goat == 'g13':
  g13 = pygame.image.load("goat_out.png") 
  g13_x,g13_y = move_out_goat_sub(g13_x,g13_y,moved_out_goat_count)

 elif out_goat == 'g14':
  g14 = pygame.image.load("goat_out.png") 
  g14_x,g14_y = move_out_goat_sub(g14_x,g14_y,moved_out_goat_count)

 elif out_goat == 'g15':
  g15 = pygame.image.load("goat_out.png") 
  g15_x,g15_y = move_out_goat_sub(g15_x,g15_y,moved_out_goat_count)

 elif out_goat == 'g16':
  g16 = pygame.image.load("goat_out.png") 
  g16_x,g16_y = move_out_goat_sub(g16_x,g16_y,moved_out_goat_count)

 elif out_goat == 'g17':
  g17 = pygame.image.load("goat_out.png") 
  g17_x,g17_y = move_out_goat_sub(g17_x,g17_y,moved_out_goat_count)

 elif out_goat == 'g18':
  g18 = pygame.image.load("goat_out.png") 
  g18_x,g18_y = move_out_goat_sub(g18_x,g18_y,moved_out_goat_count)

 elif out_goat == 'g19':
  g19 = pygame.image.load("goat_out.png") 
  g19_x,g19_y = move_out_goat_sub(g19_x,g19_y,moved_out_goat_count)

 elif out_goat == 'g20':
  g20 = pygame.image.load("goat_out.png") 
  g20_x,g20_y = move_out_goat_sub(g20_x,g20_y,moved_out_goat_count)
 

def make_screen():
 #draw board
 board = pygame.image.load("board.png")
 win.blit(board,(0,0))

 #draw 25 surfaces
 win.blit(b1,(e1_x,e1_y))
 win.blit(b2,(e2_x,e2_y))
 win.blit(b3,(e3_x,e3_y))
 win.blit(b4,(e4_x,e4_y))
 win.blit(b5,(e5_x,e5_y))
 win.blit(b6,(d1_x,d1_y))
 win.blit(b7,(d2_x,d2_y))
 win.blit(b8,(d3_x,d3_y))
 win.blit(b9,(d4_x,d4_y))
 win.blit(b10,(d5_x,d5_y))
 win.blit(b11,(c1_x,c1_y))
 win.blit(b12,(c2_x,c2_y))
 win.blit(b13,(c3_x,c3_y))
 win.blit(b14,(c4_x,c4_y))
 win.blit(b15,(c5_x,c5_y))
 win.blit(b16,(b1_x,b1_y))
 win.blit(b17,(b2_x,b2_y))
 win.blit(b18,(b3_x,b3_y))
 win.blit(b19,(b4_x,b4_y))
 win.blit(b20,(b5_x,b5_y))
 win.blit(b21,(a1_x,a1_y))
 win.blit(b22,(a2_x,a2_y))
 win.blit(b23,(a3_x,a3_y))
 win.blit(b24,(a4_x,a4_y))
 win.blit(b25,(a5_x,a5_y))

 #draw 20 goats
 win.blit(g1,(g1_x,g1_y))
 win.blit(g2,(g2_x,g2_y))
 win.blit(g3,(g3_x,g3_y))
 win.blit(g4,(g4_x,g4_y))
 win.blit(g5,(g5_x,g5_y))
 win.blit(g6,(g6_x,g6_y))
 win.blit(g7,(g7_x,g7_y))
 win.blit(g8,(g8_x,g8_y))
 win.blit(g9,(g9_x,g9_y))
 win.blit(g10,(g10_x,g10_y))
 win.blit(g11,(g11_x,g11_y))
 win.blit(g12,(g12_x,g12_y))
 win.blit(g13,(g13_x,g13_y))
 win.blit(g14,(g14_x,g14_y))
 win.blit(g15,(g15_x,g15_y))
 win.blit(g16,(g16_x,g16_y))
 win.blit(g17,(g17_x,g17_y))
 win.blit(g18,(g18_x,g18_y))
 win.blit(g19,(g19_x,g19_y))
 win.blit(g20,(g20_x,g20_y))

 #draw 4 tigers
 win.blit(t1,(t1_x,t1_y))
 win.blit(t2,(t2_x,t2_y))
 win.blit(t3,(t3_x,t3_y))
 win.blit(t4,(t4_x,t4_y))



while True:
 while goat_turns:
  make_screen()
  if moved_out_goat_count == 5:
   message("Khel Khatam")                                               
   pygame.display.update() 
   time.sleep(2)
   end_attempt()
  message("Goat's Turn") 
  pygame.display.update() 

  left_for_goat = list(set(total_place)-set(tiger_space_occupied)-set(goat_space_occupied)) 
  print(goat_move_switch)

  if goat_move_switch <= 20:
   message("First phase")
   pygame.display.update()
   for event in pygame.event.get():
    if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == K_ESCAPE):
     end_attempt()
    if event.type == pygame.MOUSEBUTTONUP:
     x,y = event.pos

     if g1.get_rect(topleft = (g1_x,g1_y)).collidepoint((x,y)):     #if g1 is clicked
      if 'g1' not in temp_goat_place:                                  # if g1 is not in array temp_goat_place - once it is moved cannot move until 20 goats are moved to board , restricts this
       message("Goat1")
       g1 = pygame.image.load("goat_selected.png")                       #highlight the image
       win.blit(g1,(g1_x,g1_y))                                          #draw highlighted image
       pygame.display.update()                                           #update the display  
       g1_x_old, g1_y_old = g1_x, g1_y                                   #store coordinates og g1
       g1_x,g1_y = goat_second_click(g1_x,g1_y,left_for_goat)            #go for second click and it returns the coordinates for g1  
       g1 = pygame.image.load("goat.png")                                #unhighligh the image.. will be drawn when making screen using makescreen() 
       if g1_x != g1_x_old or g1_y != g1_y_old:                          #if new cooordinate != old coordinate 
        g_value = board_pos(g1_x,g1_y)                                    #get board position of new coordinates e.g c1    
        goat_space_occupied.append(g_value)                               #add c1 to goat_space_occupied
        temp_goat_place.append('g1')                                      #add g1 to temp_goat_place
        tiger_turn()                                                      #tigerturn() 
       elif g1_x == g1_x_old and g1_y == g1_y_old:                       #else
        message("Invalid Move")                                           #text - invalid move   
        pygame.display.update()                                           #update display
        goat_turn()                                                       #again goatturn
      elif 'g1' in temp_goat_place:                                     #elif g1 in temp_goat_place     
       goat_turn()                                                       #nothing happens, again turn of goat
 

     elif g2.get_rect(topleft = (g2_x,g2_y)).collidepoint((x,y)):
      if 'g2' not in temp_goat_place:
       message("Goat2")
       g2 = pygame.image.load("goat_selected.png")
       win.blit(g2,(g2_x,g2_y))
       pygame.display.update()      
       g2_x_old, g2_y_old = g2_x, g2_y
       g2_x,g2_y = goat_second_click(g2_x,g2_y,left_for_goat)
       g2 = pygame.image.load("goat.png")
       if g2_x != g2_x_old or g2_y != g2_y_old:
        g_value = board_pos(g2_x,g2_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g2')
        print(temp_goat_place)
        tiger_turn()
       elif g2_x == g2_x_old and g2_y == g2_y_old:
        message("Invalid Move")
        pygame.display.update()
        goat_turn()
      elif 'g2' in temp_goat_place:
       goat_turn()

     elif g3.get_rect(topleft = (g3_x,g3_y)).collidepoint((x,y)):
      if 'g3' not in temp_goat_place:
       message("Goat3")
       g3 = pygame.image.load("goat_selected.png")
       win.blit(g3,(g3_x,g3_y))
       pygame.display.update()         
       g3_x_old, g3_y_old = g3_x, g3_y
       g3_x,g3_y = goat_second_click(g3_x,g3_y,left_for_goat)
       g3 = pygame.image.load("goat.png")
       if g3_x != g3_x_old or g3_y != g3_y_old:
        g_value = board_pos(g3_x,g3_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g3')
        print(temp_goat_place)
        tiger_turn()
       elif g3_x == g3_x_old and g3_y == g3_y_old:
        message("Invalid Move")
        pygame.display.update()
        goat_turn()
      elif 'g3' in temp_goat_place:
       goat_turn()

     elif g4.get_rect(topleft = (g4_x,g4_y)).collidepoint((x,y)):
      if 'g4' not in temp_goat_place:
       message("Goat4")
       g4 = pygame.image.load("goat_selected.png")
       win.blit(g4,(g4_x,g4_y))
       pygame.display.update()         
       g4_x_old, g4_y_old = g4_x, g4_y
       g4_x,g4_y = goat_second_click(g4_x,g4_y,left_for_goat)
       g4 = pygame.image.load("goat.png")
       if g4_x != g4_x_old or g4_y != g4_y_old:
        g_value = board_pos(g4_x,g4_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g4')
        print(temp_goat_place)
        tiger_turn()
       elif g4_x == g4_x_old and g4_y == g4_y_old:
        message("Invalid Move")
        pygame.display.update()
        goat_turn()
      elif 'g4' in temp_goat_place:
       goat_turn() 

     elif g5.get_rect(topleft = (g5_x,g5_y)).collidepoint((x,y)):
      if 'g5' not in temp_goat_place:
       message("Goat1")
       g5 = pygame.image.load("goat_selected.png")
       win.blit(g5,(g5_x,g5_y))
       pygame.display.update()         
       g5_x_old, g5_y_old = g5_x, g5_y
       g5_x,g5_y = goat_second_click(g5_x,g5_y,left_for_goat)
       g5 = pygame.image.load("goat.png")
       if g5_x != g5_x_old or g5_y != g5_y_old:
        g_value = board_pos(g5_x,g5_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g5')
        print(temp_goat_place)
        tiger_turn()
       elif g5_x == g5_x_old and g5_y == g5_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g5' in temp_goat_place:
       goat_turn()

     elif g6.get_rect(topleft = (g6_x,g6_y)).collidepoint((x,y)):
      if 'g6' not in temp_goat_place:
       message("Goat6")
       g6 = pygame.image.load("goat_selected.png")
       win.blit(g6,(g6_x,g6_y))
       pygame.display.update()        
       g6_x_old, g6_y_old = g6_x, g6_y
       g6_x,g6_y = goat_second_click(g6_x,g6_y,left_for_goat)
       g6 = pygame.image.load("goat.png")
       if g6_x != g6_x_old or g6_y != g6_y_old:
        g_value = board_pos(g6_x,g6_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g6')
        print(temp_goat_place)
        tiger_turn()
       elif g6_x == g6_x_old and g6_y == g6_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g6' in temp_goat_place:
       goat_turn()

     elif g7.get_rect(topleft = (g7_x,g7_y)).collidepoint((x,y)):
      if 'g7' not in temp_goat_place:
       message("Goat7")
       g7 = pygame.image.load("goat_selected.png")
       win.blit(g7,(g7_x,g7_y))
       pygame.display.update()         
       g7_x_old, g7_y_old = g7_x, g7_y
       g7_x,g7_y = goat_second_click(g7_x,g7_y,left_for_goat)
       g7 = pygame.image.load("goat.png")
       if g7_x != g7_x_old or g7_y != g7_y_old:
        g_value = board_pos(g7_x,g7_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g7')
        print(temp_goat_place)
        tiger_turn()
       elif g7_x == g7_x_old and g7_y == g7_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g7' in temp_goat_place:
       goat_turn()

     elif g8.get_rect(topleft = (g8_x,g8_y)).collidepoint((x,y)):
      if 'g8' not in temp_goat_place:
       message("Goat8")
       g8 = pygame.image.load("goat_selected.png")
       win.blit(g8,(g8_x,g8_y))
      pygame.display.update()        
      g8_x_old, g8_y_old = g8_x, g8_y
      g8_x,g8_y = goat_second_click(g8_x,g8_y,left_for_goat)
      g8 = pygame.image.load("goat.png")
      if g8_x != g8_x_old or g8_y != g8_y_old:
       g_value = board_pos(g8_x,g8_y)
       goat_space_occupied.append(g_value) 
       print(goat_space_occupied)
       temp_goat_place.append('g8')
       tiger_turn()
      elif g8_x == g8_x_old and g8_y == g8_y_old:
       message("Invalid Move")
       pygame.display.update() 
       goat_turn()
      elif 'g8' in temp_goat_place:
       goat_turn()

     elif g9.get_rect(topleft = (g9_x,g9_y)).collidepoint((x,y)):
      if 'g9' not in temp_goat_place:
       message("Goat9")
       g9 = pygame.image.load("goat_selected.png")
       win.blit(g9,(g9_x,g9_y))
       pygame.display.update()         
       g9_x_old, g9_y_old = g9_x, g9_y
       g9_x,g9_y = goat_second_click(g9_x,g9_y,left_for_goat)
       g9 = pygame.image.load("goat.png")
       if g9_x != g9_x_old or g9_y != g9_y_old:
        g_value = board_pos(g9_x,g9_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g9')
        print(temp_goat_place)
        tiger_turn()
       elif g9_x == g9_x_old and g9_y == g9_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g9' in temp_goat_place:
       goat_turn()

     elif g10.get_rect(topleft = (g10_x,g10_y)).collidepoint((x,y)):
      if 'g10' not in temp_goat_place:
       message("Goat10")
       g10 = pygame.image.load("goat_selected.png")
       win.blit(g10,(g10_x,g10_y))
       pygame.display.update()        
       g10_x_old, g10_y_old = g10_x, g10_y
       g10_x,g10_y = goat_second_click(g10_x,g10_y,left_for_goat)
       g10 = pygame.image.load("goat.png")
       if g10_x != g10_x_old or g10_y != g10_y_old:
        g_value = board_pos(g10_x,g10_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g10')
        print(temp_goat_place)
        tiger_turn()
       elif g10_x == g10_x_old and g10_y == g10_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g10' in temp_goat_place:
       goat_turn() 

     elif g11.get_rect(topleft = (g11_x,g11_y)).collidepoint((x,y)):
      if 'g11' not in temp_goat_place:
       message("Goat11")
       g11 = pygame.image.load("goat_selected.png")
       win.blit(g11,(g11_x,g11_y))
       pygame.display.update()         
       g11_x_old, g11_y_old = g11_x, g11_y
       g11_x,g11_y = goat_second_click(g11_x,g11_y,left_for_goat)
       g11 = pygame.image.load("goat.png")
       if g11_x != g11_x_old or g11_y != g11_y_old:
        g_value = board_pos(g11_x,g11_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g11')
        print(temp_goat_place)
        tiger_turn()
       elif g11_x == g11_x_old and g11_y == g11_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g11' in temp_goat_place:
       goat_turn() 

     elif g12.get_rect(topleft = (g12_x,g12_y)).collidepoint((x,y)):
      if 'g12' not in temp_goat_place:
       message("Goat12")
       g12 = pygame.image.load("goat_selected.png")
       win.blit(g12,(g12_x,g12_y))
       pygame.display.update()         
       g12_x_old, g12_y_old = g12_x, g12_y
       g12_x,g12_y = goat_second_click(g12_x,g12_y,left_for_goat)
       g12 = pygame.image.load("goat.png")
       if g12_x != g12_x_old or g12_y != g12_y_old:
        g_value = board_pos(g12_x,g12_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g12')
        print(temp_goat_place)
        tiger_turn()
       elif g12_x == g12_x_old and g12_y == g12_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g12' in temp_goat_place:
       goat_turn() 

     elif g13.get_rect(topleft = (g13_x,g13_y)).collidepoint((x,y)):
      if 'g13' not in temp_goat_place:
       message("Goat13")
       g13 = pygame.image.load("goat_selected.png")
       win.blit(g13,(g13_x,g13_y))
       pygame.display.update()        
       g13_x_old, g13_y_old = g13_x, g13_y
       g13_x,g13_y = goat_second_click(g13_x,g13_y,left_for_goat)
       g13 = pygame.image.load("goat.png")
       if g13_x != g13_x_old or g13_y != g13_y_old:
        g_value = board_pos(g13_x,g13_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g13')
        print(temp_goat_place)
        tiger_turn()
       elif g13_x == g13_x_old and g13_y == g13_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g13' in temp_goat_place:
       goat_turn() 

     elif g14.get_rect(topleft = (g14_x,g14_y)).collidepoint((x,y)):
      if 'g14' not in temp_goat_place:
       message("Goat14")
       g14 = pygame.image.load("goat_selected.png")
       win.blit(g14,(g14_x,g14_y))
       pygame.display.update()         
       g14_x_old, g14_y_old = g14_x, g14_y
       g14_x,g14_y = goat_second_click(g14_x,g14_y,left_for_goat)
       g14 = pygame.image.load("goat.png")
       if g14_x != g14_x_old or g14_y != g14_y_old:
        g_value = board_pos(g14_x,g14_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g14')
        print(temp_goat_place)
        tiger_turn()
       elif g14_x == g14_x_old and g14_y == g14_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g14' in temp_goat_place:
       goat_turn() 

     elif g15.get_rect(topleft = (g15_x,g15_y)).collidepoint((x,y)):
      if 'g15' not in temp_goat_place:
       message("Goat15")
       g15 = pygame.image.load("goat_selected.png")
       win.blit(g15,(g15_x,g15_y))
       pygame.display.update()         
       g15_x_old, g15_y_old = g15_x, g15_y
       g15_x,g15_y = goat_second_click(g15_x,g15_y,left_for_goat)
       g15 = pygame.image.load("goat.png")
       if g15_x != g15_x_old or g15_y != g15_y_old:
        g_value = board_pos(g15_x,g15_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g15')
        print(temp_goat_place)
        tiger_turn()
       elif g15_x == g15_x_old and g15_y == g15_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g15' in temp_goat_place:
       goat_turn()

     elif g16.get_rect(topleft = (g16_x,g16_y)).collidepoint((x,y)):
      if 'g16' not in temp_goat_place:
       message("Goat16")
       g16 = pygame.image.load("goat_selected.png")
       win.blit(g16,(g16_x,g16_y))
       pygame.display.update()         
       g16_x_old, g16_y_old = g16_x, g16_y
       g16_x,g16_y = goat_second_click(g16_x,g16_y,left_for_goat)
       g16 = pygame.image.load("goat.png")
       if g16_x != g16_x_old or g16_y != g16_y_old:
        g_value = board_pos(g16_x,g16_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g16')
        print(temp_goat_place)
        tiger_turn()
       elif g16_x == g16_x_old and g16_y == g16_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g16' in temp_goat_place:
       goat_turn()

     elif g17.get_rect(topleft = (g17_x,g17_y)).collidepoint((x,y)):
      if 'g17' not in temp_goat_place:
       message("Goat17")
       g17 = pygame.image.load("goat_selected.png")
       win.blit(g17,(g17_x,g17_y))
       pygame.display.update()         
       g17_x_old, g17_y_old = g17_x, g17_y
       g17_x,g17_y = goat_second_click(g17_x,g17_y,left_for_goat)
       g17 = pygame.image.load("goat.png")
       if g17_x != g17_x_old or g17_y != g17_y_old:
        g_value = board_pos(g17_x,g17_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g17')
        print(temp_goat_place)
        tiger_turn()
       elif g17_x == g17_x_old and g17_y == g17_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g17' in temp_goat_place:
       goat_turn()

     elif g18.get_rect(topleft = (g18_x,g18_y)).collidepoint((x,y)):
      if 'g18' not in temp_goat_place:
       message("Goat18")
       g18 = pygame.image.load("goat_selected.png")
       win.blit(g18,(g18_x,g18_y))
       pygame.display.update()         
       g18_x_old, g18_y_old = g18_x, g18_y
       g18_x,g18_y = goat_second_click(g18_x,g18_y,left_for_goat)
       g18 = pygame.image.load("goat.png")
       if g18_x != g18_x_old or g18_y != g18_y_old:
        g_value = board_pos(g18_x,g18_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g18')
        print(temp_goat_place)
        tiger_turn()
       elif g18_x == g18_x_old and g18_y == g18_y_old:
        message("Invalid Move")
        pygame.display.update() 
        goat_turn()
      elif 'g18' in temp_goat_place:
       goat_turn()

     elif g19.get_rect(topleft = (g19_x,g19_y)).collidepoint((x,y)):
      if 'g19' not in temp_goat_place:
       message("Goat20")
       g19 = pygame.image.load("goat_selected.png")
       win.blit(g19,(g19_x,g19_y))
       pygame.display.update()         
       g19_x_old, g19_y_old = g19_x, g19_y
       g19_x,g19_y = goat_second_click(g19_x,g19_y,left_for_goat)
       g19 = pygame.image.load("goat.png")
       if g19_x != g19_x_old or g19_y != g19_y_old:
        g_value = board_pos(g19_x,g19_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g19')
        print(temp_goat_place)
        tiger_turn()
       elif g19_x == g19_x_old and g19_y == g19_y_old:
        message("Invalid Move")
        pygame.display.update() 
        
        goat_turn()
      elif 'g19' in temp_goat_place:
       print('not allowed')
       goat_turn()

     elif g20.get_rect(topleft = (g20_x,g20_y)).collidepoint((x,y)):
      if 'g20' not in temp_goat_place:
       message("Goat20")
       g20 = pygame.image.load("goat_selected.png")
       win.blit(g20,(g20_x,g20_y))
       pygame.display.update()         
       g20_x_old, g20_y_old = g20_x, g20_y
       g20_x,g20_y = goat_second_click(g20_x,g20_y,left_for_goat)
       g20 = pygame.image.load("goat.png")
       if g20_x != g20_x_old or g20_y != g20_y_old:
        g_value = board_pos(g20_x,g20_y)
        goat_space_occupied.append(g_value) 
        print(goat_space_occupied)
        temp_goat_place.append('g20')
        print(temp_goat_place)
        tiger_turn()
       elif g20_x == g20_x_old and g20_y == g20_y_old:
        message("Invalid Move")
        pygame.display.update()         
        goat_turn()
      elif 'g20' in temp_goat_place:
       print('not allowed')
       goat_turn()

     goat_move_switch+=1
  
  #after 20 moves of gpat
  elif goat_move_switch > 20:
   print("Second" + str(goat_move_switch))
   for event in pygame.event.get():
    if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == K_ESCAPE):
     end_attempt()
    if event.type == pygame.MOUSEBUTTONUP:
     x,y = event.pos
     if g1.get_rect(topleft = (g1_x,g1_y)).collidepoint((x,y)):   #if clicked in goat1
      message("Goat1")                                            #display Goat1
      g1 = pygame.image.load("goat_selected.png")                 #change image of goat to indicate selected
      win.blit(g1,(g1_x,g1_y))                                    #paste the change
      pygame.display.update()                                     #display update
      g1_x_old, g1_y_old = g1_x, g1_y                             #store current coordinate of goat1
      g_value = board_pos(g1_x,g1_y)                              #get the position of board eg.b1,c3
      goat_direction = poss_moves(g_value)                        #where the goat1 can move if goat is alone in a board
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied)) #filterd possible moves of goat on board
      g1_x,g1_y = goat_second_click_20plus(g1_x,g1_y,goat_possible_moves)  #get the new position of goat
      g1 = pygame.image.load("goat.png")                                   #load old image of goat
      if g1_x != g1_x_old or g1_y != g1_y_old:                             #if position changed
       goat_space_occupied.remove(g_value)                                   #remove old coordinate in list of space occupied by goat
       g_value2 = board_pos(g1_x,g1_y)                                       #get current coordinate of goat after movement
       goat_space_occupied.append(g_value2)                                  #add new coordinate in list of space occupied by goat 
       tiger_turn()                                                    #tiger turn is set true
      elif g1_x == g1_x_old and g1_y == g1_y_old:                          #if position is not changed
       message("Invalid Move")                                              #display 'Invalid Move'
       pygame.display.update()                                              #update display    
       goat_turn()                                                   #again tiger turn is set false

     elif g2.get_rect(topleft = (g2_x,g2_y)).collidepoint((x,y)):
      message("Goat2")
      g2 = pygame.image.load("goat_selected.png")
      win.blit(g2,(g2_x,g2_y))
      pygame.display.update() 
      g2_x_old, g2_y_old = g2_x, g2_y
      g_value = board_pos(g2_x,g2_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g2_x,g2_y = goat_second_click_20plus(g2_x,g2_y,goat_possible_moves)
      g2 = pygame.image.load("goat.png")
      if g2_x != g2_x_old or g2_y != g2_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g2_x,g2_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g2_x == g2_x_old and g2_y == g2_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()
     
     elif g3.get_rect(topleft = (g3_x,g3_y)).collidepoint((x,y)):
      message("Goat2")
      g3 = pygame.image.load("goat_selected.png")
      win.blit(g3,(g3_x,g3_y))
      pygame.display.update() 
      g3_x_old, g3_y_old = g3_x, g3_y
      g_value = board_pos(g3_x,g3_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g3_x,g3_y = goat_second_click_20plus(g3_x,g3_y,goat_possible_moves)
      g3 = pygame.image.load("goat.png")
      if g3_x != g3_x_old or g3_y != g3_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g3_x,g3_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g3_x == g3_x_old and g3_y == g3_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g4.get_rect(topleft = (g4_x,g4_y)).collidepoint((x,y)):
      message("Goat2")
      g4 = pygame.image.load("goat_selected.png")
      win.blit(g4,(g4_x,g4_y))
      pygame.display.update() 
      g4_x_old, g4_y_old = g4_x, g4_y
      g_value = board_pos(g4_x,g4_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g4_x,g4_y = goat_second_click_20plus(g4_x,g4_y,goat_possible_moves)
      g4 = pygame.image.load("goat.png")
      if g4_x != g4_x_old or g4_y != g4_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g4_x,g4_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g4_x == g4_x_old and g4_y == g4_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g5.get_rect(topleft = (g5_x,g5_y)).collidepoint((x,y)):
      message("Goat2")
      g5 = pygame.image.load("goat_selected.png")
      win.blit(g5,(g5_x,g5_y))
      pygame.display.update() 
      g5_x_old, g5_y_old = g5_x, g5_y
      g_value = board_pos(g5_x,g5_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g5_x,g5_y = goat_second_click_20plus(g5_x,g5_y,goat_possible_moves)
      g5 = pygame.image.load("goat.png")
      if g5_x != g5_x_old or g5_y != g5_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g5_x,g5_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g5_x == g5_x_old and g5_y == g5_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g6.get_rect(topleft = (g6_x,g6_y)).collidepoint((x,y)):
      message("Goat2")
      g6 = pygame.image.load("goat_selected.png")
      win.blit(g6,(g6_x,g6_y))
      pygame.display.update() 
      g6_x_old, g6_y_old = g6_x, g6_y
      g_value = board_pos(g6_x,g6_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g6_x,g6_y = goat_second_click_20plus(g6_x,g6_y,goat_possible_moves)
      g6 = pygame.image.load("goat.png")
      if g6_x != g6_x_old or g6_y != g6_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g6_x,g6_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g6_x == g6_x_old and g6_y == g6_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g7.get_rect(topleft = (g7_x,g7_y)).collidepoint((x,y)):
      message("Goat2")
      g7 = pygame.image.load("goat_selected.png")
      win.blit(g7,(g7_x,g7_y))
      pygame.display.update() 
      g7_x_old, g7_y_old = g7_x, g7_y
      g_value = board_pos(g7_x,g7_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g7_x,g7_y = goat_second_click_20plus(g7_x,g7_y,goat_possible_moves)
      g7 = pygame.image.load("goat.png")
      if g7_x != g7_x_old or g7_y != g7_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g7_x,g7_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g7_x == g7_x_old and g7_y == g7_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g8.get_rect(topleft = (g8_x,g8_y)).collidepoint((x,y)):
      message("Goat2")
      g8 = pygame.image.load("goat_selected.png")
      win.blit(g8,(g8_x,g8_y))
      pygame.display.update() 
      g8_x_old, g8_y_old = g8_x, g8_y
      g_value = board_pos(g8_x,g8_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g8_x,g8_y = goat_second_click_20plus(g8_x,g8_y,goat_possible_moves)
      g8 = pygame.image.load("goat.png")
      if g8_x != g8_x_old or g8_y != g8_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g8_x,g8_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g8_x == g8_x_old and g8_y == g8_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g9.get_rect(topleft = (g9_x,g9_y)).collidepoint((x,y)):
      message("Goat2")
      g9 = pygame.image.load("goat_selected.png")
      win.blit(g9,(g9_x,g9_y))
      pygame.display.update() 
      g9_x_old, g9_y_old = g9_x, g9_y
      g_value = board_pos(g9_x,g9_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g9_x,g9_y = goat_second_click_20plus(g9_x,g9_y,goat_possible_moves)
      g9 = pygame.image.load("goat.png")
      if g9_x != g9_x_old or g9_y != g9_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g9_x,g9_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g9_x == g9_x_old and g9_y == g9_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g10.get_rect(topleft = (g10_x,g10_y)).collidepoint((x,y)):
      message("Goat2")
      g10 = pygame.image.load("goat_selected.png")
      win.blit(g10,(g10_x,g10_y))
      pygame.display.update() 
      g10_x_old, g10_y_old = g10_x, g10_y
      g_value = board_pos(g10_x,g10_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g10_x,g10_y = goat_second_click_20plus(g10_x,g10_y,goat_possible_moves)
      g10 = pygame.image.load("goat.png")
      if g10_x != g10_x_old or g10_y != g10_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g10_x,g10_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g10_x == g10_x_old and g10_y == g10_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g11.get_rect(topleft = (g11_x,g11_y)).collidepoint((x,y)):
      message("Goat2")
      g11 = pygame.image.load("goat_selected.png")
      win.blit(g11,(g11_x,g11_y))
      pygame.display.update() 
      g11_x_old, g11_y_old = g11_x, g11_y
      g_value = board_pos(g11_x,g11_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g11_x,g11_y = goat_second_click_20plus(g11_x,g11_y,goat_possible_moves)
      g11 = pygame.image.load("goat.png")
      if g11_x != g11_x_old or g11_y != g11_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g11_x,g11_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g11_x == g11_x_old and g11_y == g11_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g12.get_rect(topleft = (g12_x,g12_y)).collidepoint((x,y)):
      message("Goat2")
      g12 = pygame.image.load("goat_selected.png")
      win.blit(g12,(g12_x,g12_y))
      pygame.display.update() 
      g12_x_old, g12_y_old = g12_x, g12_y
      g_value = board_pos(g12_x,g12_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g12_x,g12_y = goat_second_click_20plus(g12_x,g12_y,goat_possible_moves)
      g12 = pygame.image.load("goat.png")
      if g12_x != g12_x_old or g12_y != g12_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g12_x,g12_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g12_x == g12_x_old and g12_y == g12_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g13.get_rect(topleft = (g13_x,g13_y)).collidepoint((x,y)):
      message("Goat2")
      g13 = pygame.image.load("goat_selected.png")
      win.blit(g13,(g13_x,g13_y))
      pygame.display.update() 
      g13_x_old, g13_y_old = g13_x, g13_y
      g_value = board_pos(g13_x,g13_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g13_x,g13_y = goat_second_click_20plus(g13_x,g13_y,goat_possible_moves)
      g13 = pygame.image.load("goat.png")
      if g13_x != g13_x_old or g13_y != g13_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g13_x,g13_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g13_x == g13_x_old and g13_y == g13_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g14.get_rect(topleft = (g14_x,g14_y)).collidepoint((x,y)):
      message("Goat2")
      g14 = pygame.image.load("goat_selected.png")
      win.blit(g14,(g14_x,g14_y))
      pygame.display.update() 
      g14_x_old, g14_y_old = g14_x, g14_y
      g_value = board_pos(g14_x,g14_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g14_x,g14_y = goat_second_click_20plus(g14_x,g14_y,goat_possible_moves)
      g14 = pygame.image.load("goat.png")
      if g14_x != g14_x_old or g14_y != g14_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g14_x,g14_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g14_x == g14_x_old and g14_y == g14_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g15.get_rect(topleft = (g15_x,g15_y)).collidepoint((x,y)):
      message("Goat2")
      g15 = pygame.image.load("goat_selected.png")
      win.blit(g15,(g15_x,g15_y))
      pygame.display.update() 
      g15_x_old, g15_y_old = g15_x, g15_y
      g_value = board_pos(g15_x,g15_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g15_x,g15_y = goat_second_click_20plus(g15_x,g15_y,goat_possible_moves)
      g15 = pygame.image.load("goat.png")
      if g15_x != g15_x_old or g15_y != g15_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g15_x,g15_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g15_x == g15_x_old and g15_y == g15_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g16.get_rect(topleft = (g16_x,g16_y)).collidepoint((x,y)):
      message("Goat2")
      g16 = pygame.image.load("goat_selected.png")
      win.blit(g16,(g16_x,g16_y))
      pygame.display.update() 
      g16_x_old, g16_y_old = g16_x, g16_y
      g_value = board_pos(g16_x,g16_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g16_x,g16_y = goat_second_click_20plus(g16_x,g16_y,goat_possible_moves)
      g16 = pygame.image.load("goat.png")
      if g16_x != g16_x_old or g16_y != g16_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g16_x,g16_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g16_x == g16_x_old and g16_y == g16_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g17.get_rect(topleft = (g17_x,g17_y)).collidepoint((x,y)):
      message("Goat2")
      g17 = pygame.image.load("goat_selected.png")
      win.blit(g17,(g17_x,g17_y))
      pygame.display.update() 
      g17_x_old, g17_y_old = g17_x, g17_y
      g_value = board_pos(g17_x,g17_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g17_x,g17_y = goat_second_click_20plus(g17_x,g17_y,goat_possible_moves)
      g17 = pygame.image.load("goat.png")
      if g17_x != g17_x_old or g17_y != g17_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g17_x,g17_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g17_x == g17_x_old and g17_y == g17_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g18.get_rect(topleft = (g18_x,g18_y)).collidepoint((x,y)):
      message("Goat2")
      g18 = pygame.image.load("goat_selected.png")
      win.blit(g18,(g18_x,g18_y))
      pygame.display.update() 
      g18_x_old, g18_y_old = g18_x, g18_y
      g_value = board_pos(g18_x,g18_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g18_x,g18_y = goat_second_click_20plus(g18_x,g18_y,goat_possible_moves)
      g18 = pygame.image.load("goat.png")
      if g18_x != g18_x_old or g18_y != g18_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g18_x,g18_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g18_x == g18_x_old and g18_y == g18_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()

     elif g19.get_rect(topleft = (g19_x,g19_y)).collidepoint((x,y)):
      message("Goat2")
      g19 = pygame.image.load("goat_selected.png")
      win.blit(g19,(g19_x,g19_y))
      pygame.display.update() 
      g19_x_old, g19_y_old = g19_x, g19_y
      g_value = board_pos(g19_x,g19_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g19_x,g19_y = goat_second_click_20plus(g19_x,g19_y,goat_possible_moves)
      g19 = pygame.image.load("goat.png")
      if g19_x != g19_x_old or g19_y != g19_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g19_x,g19_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g19_x == g19_x_old and g19_y == g19_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()


     elif g20.get_rect(topleft = (g20_x,g20_y)).collidepoint((x,y)):
      message("Goat2")
      g20 = pygame.image.load("goat_selected.png")
      win.blit(g20,(g20_x,g20_y))
      pygame.display.update() 
      g20_x_old, g20_y_old = g20_x, g20_y
      g_value = board_pos(g20_x,g20_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g20_x,g20_y = goat_second_click_20plus(g20_x,g20_y,goat_possible_moves)
      g20 = pygame.image.load("goat.png")
      if g20_x != g20_x_old or g20_y != g20_y_old:
       goat_space_occupied.remove(g_value)
       g_value2 = board_pos(g20_x,g20_y)
       goat_space_occupied.append(g_value2)
       tiger_turn()
      elif g20_x == g20_x_old and g20_y == g20_y_old:
       message("Invalid Move")
       pygame.display.update()
       goat_turn()
     goat_move_switch += 1 
  
  pygame.display.update()
  clock.tick(100)


 while tiger_turns:
  make_screen()
  message("Tiger's Turn")
  pygame.display.update() 
  for event in pygame.event.get():
    if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == K_ESCAPE):
     end_attempt()
    if event.type == pygame.MOUSEBUTTONUP:
     x,y = event.pos
     if t1.get_rect(topleft = (t1_x,t1_y)).collidepoint((x,y)):           #if clicked in tiger1
      message("t1")
      t1 = pygame.image.load("tiger_selected.png")                        #load selected image for tiger
      win.blit(t1,(t1_x,t1_y))                                            #draw in screen
      pygame.display.update()                                             #display update
      t1_x_old, t1_y_old = t1_x, t1_y                                     #store coordinate of tiger in board
      t_value = board_pos(t1_x,t1_y)                                      #find the old position of tiger in the board
      tiger_direction = poss_moves(t_value)                                 #find the possible moves of tiger in board from above position if tiger is alone in the board
      goat_interrupt = list(set(tiger_direction)&set(goat_space_occupied)) #goats around tiger in board
      left_for_tiger = list(set(tiger_direction)-set(goat_interrupt))	    #possible moves for tiger execpt jump
      jump_move = []                                                        #to store moves where tiger can jump
      dict_improved_move = {}                                               #dictionary to store the goat around tiger and possible jump state
      for i in range(0,len(goat_interrupt)):                               #iteration 0 to length of list of position of goats minus 1, if len = 0 then passes
        new_possible_move = tiger_newmove(t_value, goat_interrupt[i])       #gets new jump move of tiger -> get possible jump pos one by one... send(tiger pos, goat pos)
        dict_improved_move[new_possible_move] = goat_interrupt[i]         #store the goat around tiger and possible jump state
        if not new_possible_move == None:                                   #if new position is returned it runs
         jump_move.append(new_possible_move)                           #new position of tiger added to the list
      print(dict_improved_move)                                         
      left_for_tiger_2 = list((set(left_for_tiger)|set(jump_move))-set(goat_space_occupied)-set(tiger_space_occupied)) #possible move of tiger in board.. cannot jump if goat available
      t1_x,t1_y = tiger_second_click(t1_x,t1_y,left_for_tiger_2)             # gets the movable position of tiger based on click
      t1= pygame.image.load("tiger.png")                                   #load old image of tiger
      if t1_x != t1_x_old or t1_y != t1_y_old:                             #if coordinates changed    
       new_tiger_pos = board_pos(t1_x,t1_y)                                 #get new position of tiger 
       if new_tiger_pos in jump_move:                                         #if new pos of tiger is in jump move
        out_goat_value_pos = dict_improved_move[new_tiger_pos]                    #out goat is the skipped goat
        x,y = get_animal_coordinate(out_goat_value_pos)                           #get the coordinates of the goat 
        out_goat = get_animal(x,y)                                                #convert coordinate to specific goat i.e g1,g2
        print("Out goat:" + str(out_goat))
        print(out_goat) 
        move_out_goat()                                                           #action for move out goat
        print(moved_out_goat_count)
        goat_space_occupied.remove(out_goat_value_pos)                            #removing out goat position from the list of goat in board
        print("Out goat position: " + str(out_goat_value_pos))
       tiger_space_occupied.remove(t_value)                                     #remove old position from list of tiger pos in board   
       t_value2 = board_pos(t1_x,t1_y)                                          #gets new tiger position in board
       tiger_space_occupied.append(t_value2)                                    #add new tiger board position in the list od tiger position
       print(tiger_space_occupied)
       goat_turn()                                                              #goat turn
      elif t1_x == t1_x_old and t1_y == t1_y_old:                           #if coordinates not changed 
       message("Invalid Move")                                                  #display 'invalid move' 
       pygame.display.update()                                                  #display update
       tiger_turn()                                                             #tiger turn

     #same logic for 4 tigers
     elif t2.get_rect(topleft = (t2_x,t2_y)).collidepoint((x,y)):           
      message("t2")
      t2 = pygame.image.load("tiger_selected.png")                        
      win.blit(t2,(t2_x,t2_y))                                            
      pygame.display.update()                                             
      t2_x_old, t2_y_old = t2_x, t2_y                                     
      t_value = board_pos(t2_x,t2_y)                                      
      tiger_direction = poss_moves(t_value)                                  
      goat_interrupt = list(set(tiger_direction)&set(goat_space_occupied)) 
      left_for_tiger = list(set(tiger_direction)-set(goat_interrupt))
      jump_move = []                                                        
      dict_improved_move = {}                                               
      for i in range(0,len(goat_interrupt)):                            
        new_possible_move = tiger_newmove(t_value, goat_interrupt[i])      
        dict_improved_move[new_possible_move] = goat_interrupt[i]         
        if not new_possible_move == None:                                   
         jump_move.append(new_possible_move)                           
      print(dict_improved_move)                                         
      left_for_tiger_2 = list((set(left_for_tiger)|set(jump_move))-set(goat_space_occupied)-set(tiger_space_occupied)) 
      t2_x,t2_y = tiger_second_click(t2_x,t2_y,left_for_tiger_2)            
      t2= pygame.image.load("tiger.png")                                   
      if t2_x != t2_x_old or t2_y != t2_y_old:                            
       new_tiger_pos = board_pos(t2_x,t2_y)                             
       if new_tiger_pos in jump_move:                                      
        out_goat_value_pos = dict_improved_move[new_tiger_pos]               
        x,y = get_animal_coordinate(out_goat_value_pos)                           
        out_goat = get_animal(x,y)                                               
        print("Out goat:" + str(out_goat))
        print(out_goat) 
        move_out_goat()                                                         
        print(moved_out_goat_count)
        goat_space_occupied.remove(out_goat_value_pos)                            
        print("Out goat position: " + str(out_goat_value_pos))
       tiger_space_occupied.remove(t_value)                                    
       t_value2 = board_pos(t2_x,t2_y)                                       
       tiger_space_occupied.append(t_value2)                             
       print(tiger_space_occupied)
       goat_turn()                                                            
      elif t2_x == t2_x_old and t2_y == t2_y_old:                           
       message("Invalid Move")                                                
       pygame.display.update()                                              
       tiger_turn()                                                           

     elif t3.get_rect(topleft = (t3_x,t3_y)).collidepoint((x,y)):           
      message("t3")
      t3 = pygame.image.load("tiger_selected.png")                        
      win.blit(t3,(t3_x,t3_y))                                            
      pygame.display.update()                                             
      t3_x_old, t3_y_old = t3_x, t3_y                                     
      t_value = board_pos(t3_x,t3_y)                                      
      tiger_direction = poss_moves(t_value)                                  
      goat_interrupt = list(set(tiger_direction)&set(goat_space_occupied)) 
      left_for_tiger = list(set(tiger_direction)-set(goat_interrupt))
      jump_move = []                                                        
      dict_improved_move = {}                                               
      for i in range(0,len(goat_interrupt)):                            
        new_possible_move = tiger_newmove(t_value, goat_interrupt[i])      
        dict_improved_move[new_possible_move] = goat_interrupt[i]         
        if not new_possible_move == None:                                   
         jump_move.append(new_possible_move)                           
      print(dict_improved_move)                                         
      left_for_tiger_2 = list((set(left_for_tiger)|set(jump_move))-set(goat_space_occupied)-set(tiger_space_occupied)) 
      t3_x,t3_y = tiger_second_click(t3_x,t3_y,left_for_tiger_2)            
      t3= pygame.image.load("tiger.png")                                   
      if t3_x != t3_x_old or t3_y != t3_y_old:                            
       new_tiger_pos = board_pos(t3_x,t3_y)                             
       if new_tiger_pos in jump_move:                                      
        out_goat_value_pos = dict_improved_move[new_tiger_pos]               
        x,y = get_animal_coordinate(out_goat_value_pos)                           
        out_goat = get_animal(x,y)                                               
        print("Out goat:" + str(out_goat))
        print(out_goat) 
        move_out_goat()                                                         
        print(moved_out_goat_count)
        goat_space_occupied.remove(out_goat_value_pos)                            
        print("Out goat position: " + str(out_goat_value_pos))
       tiger_space_occupied.remove(t_value)                                    
       t_value2 = board_pos(t3_x,t3_y)                                       
       tiger_space_occupied.append(t_value2)                             
       print(tiger_space_occupied)
       goat_turn()                                                            
      elif t3_x == t3_x_old and t3_y == t3_y_old:                           
       message("Invalid Move")                                                
       pygame.display.update()                                              
       tiger_turn()                                                           

     elif t4.get_rect(topleft = (t4_x,t4_y)).collidepoint((x,y)):           
      message("t4")
      t4 = pygame.image.load("tiger_selected.png")                        
      win.blit(t4,(t4_x,t4_y))                                            
      pygame.display.update()                                             
      t4_x_old, t4_y_old = t4_x, t4_y                                     
      t_value = board_pos(t4_x,t4_y)                                      
      tiger_direction = poss_moves(t_value)                                  
      goat_interrupt = list(set(tiger_direction)&set(goat_space_occupied)) 
      left_for_tiger = list(set(tiger_direction)-set(goat_interrupt))
      jump_move = []                                                        
      dict_improved_move = {}                                               
      for i in range(0,len(goat_interrupt)):                            
        new_possible_move = tiger_newmove(t_value, goat_interrupt[i])      
        dict_improved_move[new_possible_move] = goat_interrupt[i]         
        if not new_possible_move == None:                                   
         jump_move.append(new_possible_move)                           
      print(dict_improved_move)                                         
      left_for_tiger_2 = list((set(left_for_tiger)|set(jump_move))-set(goat_space_occupied)-set(tiger_space_occupied)) 
      t4_x,t4_y = tiger_second_click(t4_x,t4_y,left_for_tiger_2)            
      t4= pygame.image.load("tiger.png")                                   
      if t4_x != t4_x_old or t4_y != t4_y_old:                            
       new_tiger_pos = board_pos(t4_x,t4_y)                             
       if new_tiger_pos in jump_move:                                      
        out_goat_value_pos = dict_improved_move[new_tiger_pos]               
        x,y = get_animal_coordinate(out_goat_value_pos)                           
        out_goat = get_animal(x,y)                                               
        print("Out goat:" + str(out_goat))
        print(out_goat) 
        move_out_goat()                                                         
        print(moved_out_goat_count)
        goat_space_occupied.remove(out_goat_value_pos)                            
        print("Out goat position: " + str(out_goat_value_pos))
       tiger_space_occupied.remove(t_value)                                    
       t_value2 = board_pos(t4_x,t4_y)                                       
       tiger_space_occupied.append(t_value2)                             
       print(tiger_space_occupied)
       goat_turn()                                                            
      elif t4_x == t4_x_old and t4_y == t4_y_old:                           
       message("Invalid Move")                                                
       pygame.display.update()                                              
       tiger_turn()                                                           

  pygame.display.update()
  clock.tick(100)


