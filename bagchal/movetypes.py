#we have either eight or four moves
#return possible moves for animal, assumes it is alone in board

def poss_moves(a): #a->current position
 result =[]

 if ((int(ord(a[0])) %2 !=0) and (int(a[1:]) %2 !=0)) or ((int(ord(a[0])) %2 ==0) and (int(a[1:]) %2 ==0)): 
 #odd odd , even even case for 8 moves
  b1 = chr(ord(a[0])+0) + str( int(a[1:])+1)
  if  97 <= ord(b1[0]) <= 101 and 1<= int(b1[1:]) <= 5:
   result.append(b1)

  b2 = chr(ord(a[0])-0) + str( int(a[1:])-1)
  if  97 <= ord(b2[0]) <= 101 and 1<= int(b2[1:]) <= 5:
   result.append(b2)

  b3 = chr(ord(a[0])+1) + str( int(a[1:])-0)
  if  97 <= ord(b3[0]) <= 101 and 1<= int(b3[1:]) <= 5:
   result.append(b3)

  b4 = chr(ord(a[0])-1) + str( int(a[1:])+0)
  if  97 <= ord(b4[0]) <= 101 and 1<= int(b4[1:]) <= 5:
   result.append(b4)

  b5 = chr(ord(a[0])+1) + str( int(a[1:])+1)
  if  97 <= ord(b5[0]) <= 101 and 1<= int(b5[1:]) <= 5:
   result.append(b5)

  b6 = chr(ord(a[0])-1) + str( int(a[1:])-1)
  if  97 <= ord(b6[0]) <= 101 and 1<= int(b6[1:]) <= 5:
   result.append(b6)

  b7 = chr(ord(a[0])+1) + str( int(a[1:])-1)
  if  97 <= ord(b7[0]) <= 101 and 1<= int(b7[1:]) <= 5:
   result.append(b7)

  b8 = chr(ord(a[0])-1) + str( int(a[1])+1)
  if  97 <= ord(b8[0]) <= 101 and 1<= int(b8[1:]) <= 5:
   result.append(b8)

 elif ((int(ord(a[0])) %2 !=0) and (int(a[1:]) %2 ==0)) or ((int(ord(a[0])) %2 ==0) and (int(a[1:]) %2 !=0)):
 #odd even, even odd case for 4 moves
  b1 = chr(ord(a[0])+0) + str( int(a[1:])+1)
  if  97 <= ord(b1[0]) <= 101 and 1<= int(b1[1:]) <= 5:
   result.append(b1)

  b2 = chr(ord(a[0])-0) + str( int(a[1:])-1)
  if  97 <= ord(b2[0]) <= 101 and 1<= int(b2[1:]) <= 5:
   result.append(b2)

  b3 = chr(ord(a[0])+1) + str( int(a[1:])-0)
  if  97 <= ord(b3[0]) <= 101 and 1<= int(b3[1:]) <= 5:
   result.append(b3)

  b4 = chr(ord(a[0])-1) + str( int(a[1:])+0)
  if  97 <= ord(b4[0]) <= 101 and 1<= int(b4[1:]) <= 5:
   result.append(b4)

 return result






















