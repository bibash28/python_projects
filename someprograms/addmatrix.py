a = [[1,2,3],
     [4,5,6]]
b = [[4,5,6],
     [7,8,9]]
c = [[0,0,0],
     [0,0,0]]

for i in range(len(a)): #iterate through rows
 for j in range(len(a[0])):  #iterate through column
   c[i][j] = a[i][j]+b[i][j]

for k in c:
 print(k)



print("Calculating entire sum of matrix")
totalsum = 0
rowsum = [[0,0,0],
     [0,0,0]]

for i in range(len(a)):
 rowsum[i]=0
 for j in range(len(a[0])):
  rowsum[i]+=a[i][j]
  totalsum+=a[i][j]  #or totalsum+=roesum[i] outside j loop

print(totalsum)


