a = input("Enter the current position: ")
result =[]


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

print("Possible positions: "+ str(result))
print("No. of possible positions: " + str(len(result)))
