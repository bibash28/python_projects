#only work for sorted array
def binarysearch(array,key):
 low = 0
 high = len(array)-1

 while low<=high:
  mid = (high+low)//2
  if array[i] == key:
   return True
  elif key < array[mid]:
   high = mid -1
  elif  key > array[mid]:
   low = mid +1

 return False
