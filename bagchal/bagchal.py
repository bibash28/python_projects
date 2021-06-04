import pygame
import time
from random import choice
from position import board_pos
from stringtovalueposition import board_value
from movetypes import poss_moves
from goatmovement import goat_second_click_20plus, goat_second_click
from tigermovement import tiger_second_click
from tigerjump import tiger_newmove
from boardtoanimalconverter import get_animal_coordinate #, get_animal

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
brown = (165,42,42)

win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("BagChal")
clock = pygame.time.Clock()

#sound
move = pygame.mixer.Sound('move.wav')
jump = pygame.mixer.Sound('jump.wav')

#at first
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
tiger_trapped = []
goat_move_switch = 1


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

#16goat
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
  texts = font.render(text,True,brown)
  win.blit(texts, (416,700))

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


def get_animal(x,y):    #returns the animal present in the x,y place of the board          
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

def move_out_goat_sub(a,b,i):     #place the out goat
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

def tiger_trap_check():            #check whether the tiger is trapped or not
 global t1_x, t1_y, t2_x, t2_y, t3_x, t3_y, t4_x, t4_y
 global t1, t2, t3, t4
 global goat_space_occupied, tiger_space_occupied
 global t1_trapped, t2_trapped, t3_trapped, t4_trapped

 t1_pos = board_pos(t1_x,t1_y) 
 print(t1_pos)
 t1_pos_move = poss_moves(t1_pos)
 for i in range(0,len(t1_pos_move)):
   t1_pos_jump = tiger_newmove(t1_pos,t1_pos_move[i])
   if t1_pos_move[i] not in tiger_space_occupied:
    if not t1_pos_jump == None: 
     t1_pos_move.append(t1_pos_jump)
 total_space_occupied_board = list(set(goat_space_occupied)|set(tiger_space_occupied))
 if len(list(set(total_space_occupied_board) & set(t1_pos_move))) == len(t1_pos_move):
   t1 = pygame.image.load("tiger_trapped.png")
   t1_trapped = 1
 else:
   t1 = pygame.image.load("tiger.png")
   t1_trapped = 0

 t2_pos = board_pos(t2_x,t2_y) 
 print(t2_pos)
 t2_pos_move = poss_moves(t2_pos)
 for i in range(0,len(t2_pos_move)):
   t2_pos_jump = tiger_newmove(t2_pos,t2_pos_move[i])
   if t2_pos_move[i] not in tiger_space_occupied:
    if not t2_pos_jump == None: 
     t2_pos_move.append(t2_pos_jump)
 total_space_occupied_board = list(set(goat_space_occupied)|set(tiger_space_occupied))
 if len(list(set(total_space_occupied_board) & set(t2_pos_move))) == len(t2_pos_move):
   t2 = pygame.image.load("tiger_trapped.png")
   t2_trapped = 2
 else:
   t2 = pygame.image.load("tiger.png")
   t2_trapped = 0

 t3_pos = board_pos(t3_x,t3_y) 
 print(t3_pos)
 t3_pos_move = poss_moves(t3_pos)
 for i in range(0,len(t3_pos_move)):
   t3_pos_jump = tiger_newmove(t3_pos,t3_pos_move[i])
   if t3_pos_move[i] not in tiger_space_occupied:
    if not t3_pos_jump == None: 
     t3_pos_move.append(t3_pos_jump)
 total_space_occupied_board = list(set(goat_space_occupied)|set(tiger_space_occupied))
 if len(list(set(total_space_occupied_board) & set(t3_pos_move))) == len(t3_pos_move):
   t3 = pygame.image.load("tiger_trapped.png")
   t3_trapped = 3
 else:
   t3 = pygame.image.load("tiger.png")
   t3_trapped = 0 

 t4_pos = board_pos(t4_x,t4_y) 
 print(t4_pos)
 t4_pos_move = poss_moves(t4_pos)
 for i in range(0,len(t4_pos_move)):
   t4_pos_jump = tiger_newmove(t4_pos,t4_pos_move[i])
   if t4_pos_move[i] not in tiger_space_occupied:
    if not t4_pos_jump == None: 
     t4_pos_move.append(t4_pos_jump)
 total_space_occupied_board = list(set(goat_space_occupied)|set(tiger_space_occupied))
 if len(list(set(total_space_occupied_board) & set(t4_pos_move))) == len(t4_pos_move):
   t4 = pygame.image.load("tiger_trapped.png")
   t4_trapped = 4
 else:
   t4 = pygame.image.load("tiger.png")
   t4_trapped = 0


def move_out_goat(out_goat):
 global g1, g2, g3, g4, g5, g6, g7, g8, g9, g10
 global g11, g12, g13, g14, g15, g16, g17, g18, g19, g20
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


def goat_phase_1(g,g_x,g_y,left_for_goat):
      global goat_move_switch
      global g1_x, g2_x, g3_x, g4_x, g5_x, g6_x, g7_x, g8_x, g9_x, g10_x, g1_y, g2_y, g3_y, g4_y, g5_y, g6_y, g7_y, g8_y, g9_y, g10_y
      global g11_x, g12_x, g13_x, g14_x, g15_x, g16_x, g17_x, g18_x, g19_x, g20_x, g11_y, g12_y, g13_y, g14_y, g15_y, g16_y, g17_y, g18_y, g19_y, g20_y 
      
      if g not in temp_goat_place:
        #message("Goat2")
        g = pygame.image.load("goat_selected.png")
        win.blit(g,(g_x,g_y))
        pygame.display.update()      
        g_x_old, g_y_old = g_x, g_y
        g_x,g_y = goat_second_click(g_x,g_y,left_for_goat)
        g = pygame.image.load("goat.png")

        if g_x != g_x_old or g_y != g_y_old:
           move.play()
           goat_move_switch+=1
           print(goat_move_switch)
           g_value = board_pos(g_x,g_y)
           goat_space_occupied.append(g_value) 
         
           if g_x_old == g1_x and g_y_old == g1_y:
             g1_x, g1_y = g_x, g_y 
             temp_goat_place.append('g1')     
           elif g_x_old == g2_x and g_y_old == g2_y:
             g2_x, g2_y = g_x, g_y 
             temp_goat_place.append('g2')
           elif g_x_old == g3_x and g_y_old == g3_y:
             g3_x, g3_y = g_x, g_y 
             temp_goat_place.append('g3')
           elif g_x_old == g4_x and g_y_old == g4_y:
             g4_x, g4_y = g_x, g_y 
             temp_goat_place.append('g4') 
           elif g_x_old == g5_x and g_y_old == g5_y:
             g5_x, g5_y = g_x, g_y 
             temp_goat_place.append('g5') 
           elif g_x_old == g6_x and g_y_old == g6_y:
             g6_x, g6_y = g_x, g_y 
             temp_goat_place.append('g6') 
           elif g_x_old == g7_x and g_y_old == g7_y:
             g7_x, g7_y = g_x, g_y 
             temp_goat_place.append('g7') 
           elif g_x_old == g8_x and g_y_old == g8_y:
             g8_x, g8_y = g_x, g_y 
             temp_goat_place.append('g8') 
           elif g_x_old == g9_x and g_y_old == g9_y:
             g9_x, g9_y = g_x, g_y 
             temp_goat_place.append('g9') 
           elif g_x_old == g10_x and g_y_old == g10_y:
             g10_x, g10_y = g_x, g_y 
             temp_goat_place.append('g10') 
           elif g_x_old == g11_x and g_y_old == g11_y:
             g11_x, g11_y = g_x, g_y 
             temp_goat_place.append('g11') 
           elif g_x_old == g12_x and g_y_old == g12_y:
             g12_x, g12_y = g_x, g_y 
             temp_goat_place.append('g12') 
           elif g_x_old == g13_x and g_y_old == g13_y:
             g13_x, g13_y = g_x, g_y 
             temp_goat_place.append('g13') 
           elif g_x_old == g14_x and g_y_old == g14_y:
             g14_x, g14_y = g_x, g_y 
             temp_goat_place.append('g14') 
           elif g_x_old == g15_x and g_y_old == g15_y:
             g15_x, g15_y = g_x, g_y 
             temp_goat_place.append('g15') 
           elif g_x_old == g16_x and g_y_old == g16_y:
             g16_x, g16_y = g_x, g_y 
             temp_goat_place.append('g16') 
           elif g_x_old == g17_x and g_y_old == g17_y:
             g17_x, g17_y = g_x, g_y 
             temp_goat_place.append('g17') 
           elif g_x_old == g18_x and g_y_old == g18_y:
             g18_x, g18_y = g_x, g_y 
             temp_goat_place.append('g18') 
           elif g_x_old == g19_x and g_y_old == g19_y:
             g19_x, g19_y = g_x, g_y 
             temp_goat_place.append('g19') 
           elif g_x_old == g20_x and g_y_old == g20_y:
             g20_x, g20_y = g_x, g_y 
             temp_goat_place.append('g20')           
           tiger_turn()
        elif g_x == g_x_old and g_y == g_y_old:
           #message("Invalid Move")
           pygame.display.update()
           goat_turn()
      elif g in temp_goat_place:
       goat_turn()


def goat_phase_2(g,g_x,g_y,goat_space_occupied,tiger_space_occupied):
      global goat_move_switch
      global g1_x, g2_x, g3_x, g4_x, g5_x, g6_x, g7_x, g8_x, g9_x, g10_x, g1_y, g2_y, g3_y, g4_y, g5_y, g6_y, g7_y, g8_y, g9_y, g10_y
      global g11_x, g12_x, g13_x, g14_x, g15_x, g16_x, g17_x, g18_x, g19_x, g20_x, g11_y, g12_y, g13_y, g14_y, g15_y, g16_y, g17_y, g18_y, g19_y, g20_y 

      #message("Goat2")
      g = pygame.image.load("goat_selected.png")
      win.blit(g,(g_x,g_y))
      pygame.display.update() 
      g_x_old, g_y_old = g_x, g_y
      g_value = board_pos(g_x,g_y)
      goat_direction = poss_moves(g_value)
      goat_possible_moves = list(set(goat_direction)-set(goat_space_occupied)-set(tiger_space_occupied))
      g_x,g_y = goat_second_click_20plus(g_x,g_y,goat_possible_moves)
      g = pygame.image.load("goat.png")

      if g_x != g_x_old or g_y != g_y_old:
           move.play()
           goat_space_occupied.remove(g_value)
           g_value2 = board_pos(g_x,g_y)
           goat_space_occupied.append(g_value2)
           if g_x_old == g1_x and g_y_old == g1_y:
             g1_x, g1_y = g_x, g_y     
           elif g_x_old == g2_x and g_y_old == g2_y:
             g2_x, g2_y = g_x, g_y 
           elif g_x_old == g3_x and g_y_old == g3_y:
             g3_x, g3_y = g_x, g_y 
           elif g_x_old == g4_x and g_y_old == g4_y:
             g4_x, g4_y = g_x, g_y 
           elif g_x_old == g5_x and g_y_old == g5_y:
             g5_x, g5_y = g_x, g_y 
           elif g_x_old == g6_x and g_y_old == g6_y:
             g6_x, g6_y = g_x, g_y 
           elif g_x_old == g7_x and g_y_old == g7_y:
             g7_x, g7_y = g_x, g_y 
           elif g_x_old == g8_x and g_y_old == g8_y:
             g8_x, g8_y = g_x, g_y  
           elif g_x_old == g9_x and g_y_old == g9_y:
             g9_x, g9_y = g_x, g_y 
           elif g_x_old == g10_x and g_y_old == g10_y:
             g10_x, g10_y = g_x, g_y 
           elif g_x_old == g11_x and g_y_old == g11_y:
             g11_x, g11_y = g_x, g_y  
           elif g_x_old == g12_x and g_y_old == g12_y:
             g12_x, g12_y = g_x, g_y 
           elif g_x_old == g13_x and g_y_old == g13_y:
             g13_x, g13_y = g_x, g_y 
           elif g_x_old == g14_x and g_y_old == g14_y:
             g14_x, g14_y = g_x, g_y 
           elif g_x_old == g15_x and g_y_old == g15_y:
             g15_x, g15_y = g_x, g_y 
           elif g_x_old == g16_x and g_y_old == g16_y:
             g16_x, g16_y = g_x, g_y 
           elif g_x_old == g17_x and g_y_old == g17_y:
             g17_x, g17_y = g_x, g_y 
           elif g_x_old == g18_x and g_y_old == g18_y:
             g18_x, g18_y = g_x, g_y  
           elif g_x_old == g19_x and g_y_old == g19_y:
             g19_x, g19_y = g_x, g_y 
           elif g_x_old == g20_x and g_y_old == g20_y:
             g20_x, g20_y = g_x, g_y 
           tiger_turn()
      elif g_x == g_x_old and g_y == g_y_old:
       #message("Invalid Move")
       pygame.display.update()
       goat_turn()


def tiger_phase(t,t_x,t_y, t_trapped): 
     global t1_x, t1_y, t2_x, t2_y, t3_x, t3_y, t4_x, t4_y

     if t_trapped == 0: 
      t = pygame.image.load("tiger_selected.png")                        
      win.blit(t,(t_x,t_y))                                            
      pygame.display.update()                                             
      t_x_old, t_y_old = t_x, t_y                                     
      t_value = board_pos(t_x,t_y)                                      
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
      t_x,t_y = tiger_second_click(t_x,t_y,left_for_tiger_2)            
      t= pygame.image.load("tiger.png")   
                                
      if t_x != t_x_old or t_y != t_y_old:       
       move.play()                     
       new_tiger_pos = board_pos(t_x,t_y)                             
       if new_tiger_pos in jump_move:                                      
        out_goat_value_pos = dict_improved_move[new_tiger_pos]               
        x,y = get_animal_coordinate(out_goat_value_pos)                           
        out_goat = get_animal(x,y)                                               
        print("Out goat:" + str(out_goat))
        print(out_goat) 
        move_out_goat(out_goat)   
        move.stop()
        jump.play()                                                      
        print(moved_out_goat_count)
        goat_space_occupied.remove(out_goat_value_pos)                            
        print("Out goat position: " + str(out_goat_value_pos))
       tiger_space_occupied.remove(t_value)                                    
       t_value2 = board_pos(t_x,t_y)                                       
       tiger_space_occupied.append(t_value2)                             
       print(tiger_space_occupied)

       if t_x_old == t1_x and t_y_old == t1_y:
         t1_x, t1_y = t_x, t_y     
       elif t_x_old == t2_x and t_y_old == t2_y:
         t2_x, t2_y = t_x, t_y 
       elif t_x_old == t3_x and t_y_old == t3_y:
         t3_x, t3_y = t_x, t_y 
       elif t_x_old == t4_x and t_y_old == t4_y:
         t4_x, t4_y = t_x, t_y 
       goat_turn()  
                                                          
      elif t_x == t_x_old and t_y == t_y_old:                           
       #message("Invalid Move")                                                
       pygame.display.update()                                              
       tiger_turn() 

     else:
      tiger_turn() 

def two_player():
 global goat_move_switch
 global t1_x, t1_y, t2_x, t2_y, t3_x, t3_y, t4_x, t4_y
 
 while True:
  while goat_turns:
   tiger_trap_check()
   make_screen()
   if moved_out_goat_count == 5:
    message("Tiger Won")                                               
    pygame.display.update() 
    time.sleep(4)
    end_attempt()

   message("Goat's Turn") 
   pygame.display.update()
   left_for_goat = list(set(total_place)-set(tiger_space_occupied)-set(goat_space_occupied)) 
   print(goat_move_switch)
   if goat_move_switch <= 20:
    #message("First phase")
    pygame.display.update()
    for event in pygame.event.get():
     if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == K_ESCAPE):
      end_attempt()
     if event.type == pygame.MOUSEBUTTONUP:
      x,y = event.pos

      if g1.get_rect(topleft = (g1_x,g1_y)).collidepoint((x,y)):     #if g1 is clicked
       goat_phase_1('g1',g1_x,g1_y,left_for_goat)  

      elif g2.get_rect(topleft = (g2_x,g2_y)).collidepoint((x,y)): 
       goat_phase_1('g2',g2_x,g2_y,left_for_goat)  
  
      elif g3.get_rect(topleft = (g3_x,g3_y)).collidepoint((x,y)):
       goat_phase_1('g3',g3_x,g3_y,left_for_goat)  

      elif g4.get_rect(topleft = (g4_x,g4_y)).collidepoint((x,y)):
       goat_phase_1('g4',g4_x,g4_y,left_for_goat)  

      elif g5.get_rect(topleft = (g5_x,g5_y)).collidepoint((x,y)):
       goat_phase_1('g5',g5_x,g5_y,left_for_goat)  

      elif g6.get_rect(topleft = (g6_x,g6_y)).collidepoint((x,y)):
       goat_phase_1('g6',g6_x,g6_y,left_for_goat)  

      elif g7.get_rect(topleft = (g7_x,g7_y)).collidepoint((x,y)):
       goat_phase_1('g7',g7_x,g7_y,left_for_goat)  

      elif g8.get_rect(topleft = (g8_x,g8_y)).collidepoint((x,y)):
       goat_phase_1('g8',g8_x,g8_y,left_for_goat)  
 
      elif g9.get_rect(topleft = (g9_x,g9_y)).collidepoint((x,y)):
       goat_phase_1('g9',g9_x,g9_y,left_for_goat)  

      elif g10.get_rect(topleft = (g10_x,g10_y)).collidepoint((x,y)):
       goat_phase_1('g10',g10_x,g10_y,left_for_goat)  

      elif g11.get_rect(topleft = (g11_x,g11_y)).collidepoint((x,y)):
       goat_phase_1('g11',g11_x,g11_y,left_for_goat)  
 
      elif g12.get_rect(topleft = (g12_x,g12_y)).collidepoint((x,y)):
       goat_phase_1('g12',g12_x,g12_y,left_for_goat)  

      elif g13.get_rect(topleft = (g13_x,g13_y)).collidepoint((x,y)):
       goat_phase_1('g13',g13_x,g13_y,left_for_goat)  

      elif g14.get_rect(topleft = (g14_x,g14_y)).collidepoint((x,y)):
       goat_phase_1('g14',g14_x,g14_y,left_for_goat)  
 
      elif g15.get_rect(topleft = (g15_x,g15_y)).collidepoint((x,y)):
       goat_phase_1('g15',g15_x,g15_y,left_for_goat)  

      elif g16.get_rect(topleft = (g16_x,g16_y)).collidepoint((x,y)):
       goat_phase_1('g16',g16_x,g16_y,left_for_goat)  

      elif g17.get_rect(topleft = (g17_x,g17_y)).collidepoint((x,y)):
       goat_phase_1('g17',g17_x,g17_y,left_for_goat)  

      elif g18.get_rect(topleft = (g18_x,g18_y)).collidepoint((x,y)):
       goat_phase_1('g18',g18_x,g18_y,left_for_goat)  

      elif g19.get_rect(topleft = (g19_x,g19_y)).collidepoint((x,y)):
       goat_phase_1('g19',g19_x,g19_y,left_for_goat)  

      elif g20.get_rect(topleft = (g20_x,g20_y)).collidepoint((x,y)):
       goat_phase_1('g20',g20_x,g20_y,left_for_goat)                                               
 
   #after 20 moves of gpat
   elif goat_move_switch > 20:
    for event in pygame.event.get():
     if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == K_ESCAPE):
      end_attempt()
     if event.type == pygame.MOUSEBUTTONUP:
      x,y = event.pos
      if g1.get_rect(topleft = (g1_x,g1_y)).collidepoint((x,y)):     #if g1 is clicked
       goat_phase_2('g1',g1_x,g1_y,goat_space_occupied,tiger_space_occupied) 
 
      elif g2.get_rect(topleft = (g2_x,g2_y)).collidepoint((x,y)): 
       goat_phase_2('g2',g2_x,g2_y,goat_space_occupied,tiger_space_occupied)

      elif g3.get_rect(topleft = (g3_x,g3_y)).collidepoint((x,y)):
       goat_phase_2('g3',g3_x,g3_y,goat_space_occupied,tiger_space_occupied) 

      elif g4.get_rect(topleft = (g4_x,g4_y)).collidepoint((x,y)):
       goat_phase_2('g4',g4_x,g4_y,goat_space_occupied,tiger_space_occupied)  
 
      elif g5.get_rect(topleft = (g5_x,g5_y)).collidepoint((x,y)):
       goat_phase_2('g5',g5_x,g5_y,goat_space_occupied,tiger_space_occupied) 

      elif g6.get_rect(topleft = (g6_x,g6_y)).collidepoint((x,y)):
       goat_phase_2('g6',g6_x,g6_y,goat_space_occupied,tiger_space_occupied) 

      elif g7.get_rect(topleft = (g7_x,g7_y)).collidepoint((x,y)):
       goat_phase_2('g7',g7_x,g7_y,goat_space_occupied,tiger_space_occupied)

      elif g8.get_rect(topleft = (g8_x,g8_y)).collidepoint((x,y)):
       goat_phase_2('g8',g8_x,g8_y,goat_space_occupied,tiger_space_occupied)

      elif g9.get_rect(topleft = (g9_x,g9_y)).collidepoint((x,y)):
       goat_phase_2('g9',g9_x,g9_y,goat_space_occupied,tiger_space_occupied)

      elif g10.get_rect(topleft = (g10_x,g10_y)).collidepoint((x,y)):
       goat_phase_2('g10',g10_x,g10_y,goat_space_occupied,tiger_space_occupied)
 
      elif g11.get_rect(topleft = (g11_x,g11_y)).collidepoint((x,y)):
       goat_phase_2('g11',g11_x,g11_y,goat_space_occupied,tiger_space_occupied)

      elif g12.get_rect(topleft = (g12_x,g12_y)).collidepoint((x,y)):
       goat_phase_2('g12',g12_x,g12_y,goat_space_occupied,tiger_space_occupied)

      elif g13.get_rect(topleft = (g13_x,g13_y)).collidepoint((x,y)):
       goat_phase_2('g13',g13_x,g13_y,goat_space_occupied,tiger_space_occupied)  

      elif g14.get_rect(topleft = (g14_x,g14_y)).collidepoint((x,y)):
       goat_phase_2('g14',g14_x,g14_y,goat_space_occupied,tiger_space_occupied)  

      elif g15.get_rect(topleft = (g15_x,g15_y)).collidepoint((x,y)):
       goat_phase_2('g15',g15_x,g15_y,goat_space_occupied,tiger_space_occupied) 

      elif g16.get_rect(topleft = (g16_x,g16_y)).collidepoint((x,y)):
       goat_phase_2('g16',g16_x,g16_y,goat_space_occupied,tiger_space_occupied) 

      elif g17.get_rect(topleft = (g17_x,g17_y)).collidepoint((x,y)):
       goat_phase_2('g17',g17_x,g17_y,goat_space_occupied,tiger_space_occupied) 

      elif g18.get_rect(topleft = (g18_x,g18_y)).collidepoint((x,y)):
       goat_phase_2('g18',g18_x,g18_y,goat_space_occupied,tiger_space_occupied) 

      elif g19.get_rect(topleft = (g19_x,g19_y)).collidepoint((x,y)):
       goat_phase_2('g19',g19_x,g19_y,goat_space_occupied,tiger_space_occupied)  
 
      elif g20.get_rect(topleft = (g20_x,g20_y)).collidepoint((x,y)):
       goat_phase_2('g20',g20_x,g20_y,goat_space_occupied,tiger_space_occupied) 
      goat_move_switch += 1 
  
   pygame.display.update()
   clock.tick(100)


  while tiger_turns:
   tiger_trap_check()
   make_screen()
   if t4_trapped == 4 and t3_trapped == 3 and t2_trapped == 2 and t1_trapped == 1:
    message("Goat Won")                                               
    pygame.display.update() 
    time.sleep(4)
    end_attempt() 

   message("Tiger's Turn")
   for event in pygame.event.get():
    if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == K_ESCAPE):
     end_attempt()
    if event.type == pygame.MOUSEBUTTONUP:
     x,y = event.pos

     if t1.get_rect(topleft = (t1_x,t1_y)).collidepoint((x,y)): 
      tiger_phase('t1',t1_x,t1_y, t1_trapped)

     elif t2.get_rect(topleft = (t2_x,t2_y)).collidepoint((x,y)):   
      tiger_phase('t2',t2_x,t2_y, t2_trapped)                                                          

     elif t3.get_rect(topleft = (t3_x,t3_y)).collidepoint((x,y)):           
      tiger_phase('t3',t3_x,t3_y, t3_trapped)                                                

     elif t4.get_rect(topleft = (t4_x,t4_y)).collidepoint((x,y)):         
      tiger_phase('t4',t4_x,t4_y, t4_trapped)                                                  
    
   pygame.display.update()
   clock.tick(100)



def main():
  startscreen = pygame.image.load("startscreen.jpg")
  win.blit(startscreen ,(0,0))

  m1 = pygame.image.load("playermenu.png")
 
  while True:
    for event in pygame.event.get():
     if (event.type == pygame.QUIT) or(event.type == pygame.KEYUP and event.key == K_ESCAPE):
       end_attempt()

     if event.type == pygame.MOUSEMOTION:  
       x,y = event.pos 
       if m1.get_rect(topleft = (410,540)).collidepoint((x,y)): 
           m1 = pygame.image.load("playermenu_chosen.png")
       else:
           m1 = pygame.image.load("playermenu.png")
 
     if event.type == pygame.MOUSEBUTTONUP:
       x,y = event.pos
       if m1.get_rect(topleft = (410,540)).collidepoint((x,y)):   
           two_player()

     win.blit(m1 ,(410,540))
    pygame.display.update()
    clock.tick(100)




main()


































