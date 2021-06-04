from random import sample,choice
from time import time

def linearsearch(array,key):
 for i in range(len(array)):
  if array[i] == key:
   return True
  elif array[i] > key:
   return False
 return False

def binarysearch(array2,key2):
 low = 0
 high = len(array2)-1

 while low<=high:
  mid = (high+low)//2
  if array2[mid] == key2:
   return True
  elif key2 < array2[mid]:
   high = mid -1
  elif  key2 > array2[mid]:
   low = mid +1

 return False

def main():
 print("Recorded Time for Linear Search")
 for i in range(10000,110000,10000):
  random_num = sample(range(1000000),i)
  sorted_random_num = sorted(random_num)
  picked = choice(sorted_random_num)

  start = time( )
  linearsearch(sorted_random_num,picked)
  end = time( )
  print("Time for range %d = %f" %(i,(end-start)))

 print(" ")
 print("Recorded Time for Binary Search")
 for j in range(10000,110000,10000):
  random_num = sample(range(1000000),j)
  sorted_random_num = sorted(random_num)
  picked = choice(sorted_random_num)

  start = time( )
  binarysearch(sorted_random_num,picked)
  end = time( )
  print("Time for range %d = %f" %(j,(end-start)))

main()
