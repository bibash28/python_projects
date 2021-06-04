
#takes position of tiger and position of goat and returns the place where tiger can jump
def tiger_newmove(tiger,goat):
 if ((int(ord(tiger[0])) %2 !=0) and (int(tiger[1:]) %2 !=0)) or ((int(ord(tiger[0])) %2 ==0) and (int(tiger[1:]) %2 ==0)):
 #odd odd , even even case for 8 moves -> tiger jump
  if (str(chr(int(ord(tiger[0]))+0))+str(int(tiger[1:])+1)) == goat:
   newplace = str(chr(int(ord(goat[0]))+0))+str(int(goat[1:])+1)

  if (str(chr(int(ord(tiger[0]))-0))+str(int(tiger[1:])-1)) == goat:
   newplace = str(chr(int(ord(goat[0]))-0))+str(int(goat[1:])-1)

  if (str(chr(int(ord(tiger[0]))+1))+str(int(tiger[1:])-0)) == goat:
   newplace = str(chr(int(ord(goat[0]))+1))+str(int(goat[1:])-0)

  if (str(chr(int(ord(tiger[0]))-1))+str(int(tiger[1:])+0)) == goat:
   newplace = str(chr(int(ord(goat[0]))-1))+str(int(goat[1:])+0)

  if (str(chr(int(ord(tiger[0]))+1))+str(int(tiger[1:])+1)) == goat:
   newplace = str(chr(int(ord(goat[0]))+1))+str(int(goat[1:])+1)

  if (str(chr(int(ord(tiger[0]))-1))+str(int(tiger[1:])-1)) == goat:
   newplace = str(chr(int(ord(goat[0]))-1))+str(int(goat[1:])-1)

  if (str(chr(int(ord(tiger[0]))+1))+str(int(tiger[1:])-1)) == goat:
   newplace = str(chr(int(ord(goat[0]))+1))+str(int(goat[1:])-1)

  if (str(chr(int(ord(tiger[0]))-1))+str(int(tiger[1:])+1)) == goat:
   newplace = str(chr(int(ord(goat[0]))-1))+str(int(goat[1:])+1)


 elif ((int(ord(tiger[0])) %2 !=0) and (int(tiger[1:]) %2 ==0)) or ((int(ord(tiger[0])) %2 ==0) and (int(tiger[1:]) %2 !=0)):
  #odd even, even odd case for 4 moves ->tiger jump
  if (str(chr(int(ord(tiger[0]))+0))+str(int(tiger[1:])+1)) == goat:
   newplace = str(chr(int(ord(goat[0]))+0))+str(int(goat[1:])+1)

  if (str(chr(int(ord(tiger[0]))-0))+str(int(tiger[1:])-1)) == goat:
   newplace = str(chr(int(ord(goat[0]))-0))+str(int(goat[1:])-1)

  if (str(chr(int(ord(tiger[0]))+1))+str(int(tiger[1:])-0)) == goat:
   newplace = str(chr(int(ord(goat[0]))+1))+str(int(goat[1:])-0)

  if (str(chr(int(ord(tiger[0]))-1))+str(int(tiger[1:])+0)) == goat:
   newplace = str(chr(int(ord(goat[0]))-1))+str(int(goat[1:])+0)


 if  97 <= ord(newplace[0]) <= 101 and 1<= int(newplace[1:]) <= 5:
  return newplace


