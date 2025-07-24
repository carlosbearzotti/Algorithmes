#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimizeDecompressionSteps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ids as parameter.
#

def minimizeDecompressionSteps(ids):
    seen = set()
    steps = 0
    
    for num in sorted(set(ids), reverse=True):
        while num % 2 == 0 and num not in seen:
            seen.add(num)
            steps += 1
            num //= 2
    return steps
# Este passou em todos 1 - 15.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ids_count = int(input().strip())

    ids = []

    for _ in range(ids_count):
        ids_item = int(input().strip())
        ids.append(ids_item)

    result = minimizeDecompressionSteps(ids)

    fptr.write(str(result) + '\n')

    fptr.close()
