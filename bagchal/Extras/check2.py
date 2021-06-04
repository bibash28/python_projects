from movetypes import poss_moves
from tigerjump import newmove


occ_goat = ['c2','c4','b2','b3','b4','d2','d3','d4']
occ_tiger = ['c3']
print("The current position of the tiger is c3")

b = poss_moves(occ_tiger[0])
print("Possible moves without goat: "+ str(b))
print("No. of possible positions: " + str(len(b)))
print(" ")
print("Improved moves")

n = len(occ_goat)
print(n)
for i in range(0,5):
 c = newmove(occ_tiger[0],occ_goat[i])
 if c != None:
  b.remove(occ_goat[i])
  b.append(c)

print("Possible moves")
print(b)













