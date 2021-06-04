a = input("Enter the current position: ")
result =[]

for i in range(1,3):
 if i == 1:
  j = i+1;
 elif i ==2:
  j = i-1

 b1 = chr(ord(a[0])+i) + str( int(a[1])+j)
 if  97 <= ord(b1[0]) <= 122 and 1<= int(b1[1:]) <= 8:
    result.append(b1)

 b2 = chr(ord(a[0])-i) + str( int(a[1])-j)
 if  97 <= ord(b2[0]) <= 122 and 1<= int(b2[1:]) <= 8:
    result.append(b2)

 b3 = chr(ord(a[0])-i) + str( int(a[1])+j)
 if  97 <= ord(b3[0]) <= 122 and 1<= int(b3[1:]) <= 8:
    result.append(b3)

 b4 = chr(ord(a[0])+i) + str( int(a[1])-j)
 if  97 <= ord(b4[0]) <= 122 and 1<= int(b4[1:]) <= 8:
    result.append(b4)

print("Possible positions: "+ str(result))
print("No. of possible positions: " + str(len(result)))



