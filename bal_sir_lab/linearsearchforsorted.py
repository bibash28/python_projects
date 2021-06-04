def sortedls(array,key):
 for i in range(len(array)):
  if array[i] == key:
   return True
  elif array[i]>key: #if key is less than other no.s
   return False

 return False   #loop completes then key > all no.s

a = [5,6,7,9]
b = int(input("Enter the integer no's: "))
print(sortedls(a,b))
