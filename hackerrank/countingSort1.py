#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # max_val = max(arr)
    # int_arr = [0] * (max_val + 1) # use this if we dont need to return only 100 elements
    int_arr = [0] * 100 # always return freq array with 100 elements (according to requirements)
    
    for num in arr:
        int_arr[num] += 1
    return int_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
