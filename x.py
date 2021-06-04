#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY names as parameter.
#

def solve(names):
    # Write your code here
    names_new = []
    output = []    
    if len(names) > 0:
        for i in range(len(names)):
            if 1 <= len(names[i]) <= 10:
                 names_new.append(names[i].lower())
        
        temp = []  
        if 1 <= len(names) <= 10**5:
            if len(names_new) > 0:
                for i in range(len(names_new)):
                    x = 0
                    a = names_new[i][x]
                    while a in names_new:
                        a = names_new[i][x + 1]
                    if names_new[i] in temp:
                        temp2  = []
                        for i in range(len(temp)):
                            if names_new[i] in temp:
                                temp2.append(names_new[i])
                        a = names_new[i] + " " + str(int(len(temp2) + 1)
                        
                    output.append(a) 
                    temp.append(names_new[i])
    return output           
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    names = []

    for _ in range(n):
        names_item = input()
        names.append(names_item)

    res = solve(names)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()

