from time import time
import matplotlib.pyplot as plt
import sys
# Matrix A[i] has dimension p[i-1] x p[i]
# for i = 1..n
def MatrixChainOrder(p, i, j):
  if i == j:
   return 0
  _min = sys.maxsize
  # place parenthesis at different places
  # between first and last matrix,
  # recursively calculate count of
  # multiplications for each parenthesis
  # placement and return the minimum count
  for k in range(i, j):
   count = (MatrixChainOrder(p, i, k) + MatrixChainOrder(p, k + 1, j)
     + p[i - 1] * p[k] * p[j])
   if count < _min:
    _min = count
  # Return minimum count
  return _min
# Driver program to test above function
arr = [1,2,3,4]
length = []
timearr =[]

#main loop
for i in range(5,100000,10000):
 start_time = time()
 arr.append(i)
 s = len(arr)
 length.append(s)
 MatrixChainOrder(arr, 1, s - 1)
 endtime = time()
 timetaken = endtime - start_time
 timearr.append(timetaken)

arr1 = arr[4:]
#plotting
print("Size of matrix", arr1)
print("Time taken", timearr)
plt.plot(arr1,timearr)
plt.xlabel('Size of matrix')
plt.ylabel('Time')
plt.title('Matrix Chain Multiplication')
plt.show()
