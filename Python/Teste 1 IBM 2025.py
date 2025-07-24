#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getDistinctOneCounts' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getDistinctOneCounts(arr):
    n = len(arr)
    original_ones = sum(arr)
    distinct_counts = set()
        
    for i in range(n):
        ones = 0
        zeros = 0
        for x in range(i, n):
            if arr[x] == 1:
                ones += 1
            else: 
                zeros += 1
            delta = zeros - ones
            new_count = original_ones + delta
            distinct_counts.add(new_count)
    
    distinct_counts.add(original_ones)
    
    return len(distinct_counts)

    # esta correto porém faltou conhecimento a mais para otimização, possilvemente se trata de arrays muito extensos a partir do teste 7-15.
    # Versão Gpt ->
#     def getDistinctOneCounts_optimized(arr):
#     n = len(arr)
#     original_ones = sum(arr)
    
#     # Transformar 0 -> +1 e 1 -> -1 para calcular maior e menor delta
#     transformed = [1 if x == 0 else -1 for x in arr]
    
#     max_gain = max_kadane(transformed)
#     min_gain = min_kadane(transformed)
    
#     # O número de 1s pode variar de original_ones + min_gain até original_ones + max_gain
#     return (max_gain - min_gain + 1)

# def max_kadane(arr):
#     max_end = max_so_far = arr[0]
#     for x in arr[1:]:
#         max_end = max(x, max_end + x)
#         max_so_far = max(max_so_far, max_end)
#     return max_so_far

# def min_kadane(arr):
#     min_end = min_so_far = arr[0]
#     for x in arr[1:]:
#         min_end = min(x, min_end + x)
#         min_so_far = min(min_so_far, min_end)
#     return min_so_far

                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getDistinctOneCounts(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
