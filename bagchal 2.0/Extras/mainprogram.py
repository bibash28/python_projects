tiger_place = ['a1', 'a5', 'e5', 'e5'] #t1,t2,t3,t4
print("Old tiger places:"+ str(tiger_place))

goat_place = ['','','','','','','','','','','','','','','',''] #g1,...,g16
print("Old goat places" +str(goat_place))

goat_reserved_place = []

game_on = True
while game_on:
 print("Goat's turn")
 goat_choice = input("Choose the goat to insert(g1,g2,...,g16): ")
 goat_new_place = input("Enter the "+goat_choice+" destination: ")
 if goat_choice == 'g1':
  goat_place[1-1] =goat_new_place
 elif goat_choice == 'g2':
  goat_place[2-1] = goat_new_place
 elif goat_choice == 'g3':
  goat_place[3-1] = goat_new_place
 elif goat_choice == 'g4':
  goat_place[4-1] = goat_new_place
 elif goat_choice == 'g5':
  goat_place[5-1] = goat_new_place
 elif goat_choice == 'g6':
  goat_place[6-1] = goat_new_place
 elif goat_choice == 'g7':
  goat_place[7-0] = goat_new_place
 elif goat_choice == 'g8':
  goat_place[8-1] = goat_new_place
 elif goat_choice == 'g9':
  goat_place[9-1] = goat_new_place
 elif goat_choice == 'g10':
  goat_place[10-1] = goat_new_place
 elif goat_choice == 'g11':
  goat_place[11-1] = goat_new_place
 elif goat_choice == 'g12':
  goat_place[12-1] = goat_new_place
 elif goat_choice == 'g13':
  goat_place[13-1] = goat_new_place
 elif goat_choice == 'g14':
  goat_place[14-1] = goat_new_place
 elif goat_choice == 'g15':
  goat_place[15-1] = goat_new_place
 elif goat_choice == 'g16':
  goat_place[16-1] = goat_new_place
 print("New goat place:"+ str(goat_place))

 goat_reserved_place.append(goat_new_place)
 print(goat_reserved_place)

 #possible move for goat ----totalmove - occupied
 #two different phase ---1. before 16 moves   2. after 16 moves

 print("Tiger's turn")
 tiger_choice = input("Choose the tiger to move(t1,t2,t3,t4): ")
 tiger_new_place = input("Enter the "+tiger_choice+" destination: ")
 if tiger_choice == 't1':
  tiger_place[1-1] = tiger_new_place
 elif tiger_choice == 't2':
  tiger_place[2-1] = tiger_new_place
 elif tiger_choice == 't3':
  tiger_place[3-1] = tiger_new_place
 elif tiger_choice == 't4':
  tiger_place[4-1] = tiger_new_place
 print("New tiger place"+ str(tiger_place))

 #possible move for tige-----total move - occupied

