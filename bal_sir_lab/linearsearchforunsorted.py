a = [4,5,6,1,8,4,7,8]

key = int(input("Enter the integer to search: "))
b = 0

for i in range(len(a)):
 if a[i] == key:
  print("Found")
  b = 1

if b == 0:
  print("NotFound")
