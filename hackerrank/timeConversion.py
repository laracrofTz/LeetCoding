#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    pm_mapping = {
        '01': '13',
        '02': '14',
        '03': '15',
        '04': '16',
        '05': '17',
        '06': '18',
        '07': '19',
        '08': '20',
        '09': '21',
        '10': '22',
        '11': '23',
        '12': '12'
    }

    time = s[-2:] # AM or PM
    timing = s[:2]
    print(time, timing)
    if time == 'AM':
        if timing == '12':
            new_time = '00' + s[2:-2]
            return new_time
        else:
            return s[:-2]
    elif time == 'PM':
        new_time = pm_mapping[timing] + s[2:-2]
        return new_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
