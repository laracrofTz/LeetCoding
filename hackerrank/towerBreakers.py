#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    # player plays optimally? which means they will always choose the best scenario
    if m == 1:
        return 2
    else:
        if n%2 == 0:
            return 2
        else: 
            return 1
        
    # an explanation i found helpful from the discussion comments
    # If tower height is 1, then player 1 has no valid moves and loses immediately. 
    # If tower count is even, then player 2 can just mirror whatever player 1 does, 
    # and thus have the final move (and win) If tower count is odd, then player 1 can set one tower to 1, 
    # reducing the problem to the "count is even" above, but with player 2 making the next move 
    # (thus player 1 copies player 2), so player 1 wins.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
