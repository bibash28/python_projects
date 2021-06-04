'''
Summations Calculator
create a program that takes 3 inputs, a lower bound, an upper bound
and the expression. Calculate the sum of that range based on the
given expression and output the result.
For Example:
Input: 2 4 *2
Output: 18 (2*2 + 3*2 + 4*2)

Input: 1 5 %2
Output: 3 (1%2 + 2%2 + 3%2 + 4%2 + 5%2)
'''


a,b,c = input("Enter the format (2 4 %2): ").split()

first = int(a)
last = int(b)+1
sum = 0

for i in range(first,last):
 sum+=eval(str(i)+c)

print(sum)

