a = int(input("Enter the integer number: "))
b = 1

print("Floyd's trianlge")
for i in range(1,a+1):
 for j in range(1,i+1):
   print(b , end=" ")
   b+=1
 print("\n")

b-=1


print("Reverse Floyd's Triangle")
for i in range(a,0,-1):
 for j in range(1,i+1):
   print( b , end=" ")
   b-=1
 print("\n")

