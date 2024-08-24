#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    val = arr[-1]
    i = n - 2
    while arr[i] > val and i >= 0: 
        arr[i+1] = arr[i]
        output = list(map(str,arr))
        print(" ".join(output))
        i -= 1
    arr[i+1] = val
    output = list(map(str,arr))
    print(" ".join(output))
        
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
