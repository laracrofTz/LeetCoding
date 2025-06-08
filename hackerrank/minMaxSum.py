#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # find sum of array first, then minus each value from the total, and find min and max
    total = sum(arr)

    # old solution
    # calc_arr = []
    # for i in arr:
    #     calc_arr.append(total - i)
        
    # min_val = min(calc_arr)
    # max_val = max(calc_arr)

    # new soln
    min_val = total - max(arr)
    max_val = total - min(arr)
    
    print(f"{min_val} {max_val}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
