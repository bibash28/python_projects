def findsmall(value):
 #assume first item is the smallest
 smallest = value[0]
 #compare with other, if smallest found then swap
 for i in range(1,len(value)): #len(value)-1+1 
  if value[i]<smallest:
   smallest = value[i]

 return smallest


a = [5,6,7,8,9,1]
print("Smallest: "+str(findsmall(a)))
