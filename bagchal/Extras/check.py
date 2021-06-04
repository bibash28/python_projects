from movetypes import poss_moves

a = input("Enter the current position: ")
b = poss_moves(a)
print("Possible positions: "+ str(b))
print("No. of possible positions: " + str(len(b)))

