#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    total = len(arr)
    pos = 0
    neg = 0
    zero = 0
    
    for n in arr:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        elif n == 0:
            zero += 1
            
    pos_ratio = pos/total
    neg_ratio = neg/total
    zero_ratio = zero/total
    
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
