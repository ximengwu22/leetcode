# flake8: noqa
"""
Given an array of stock prices where prices[i] is stock price of month i , we want to find the number of stock groups that are maximumProfitable. A stock group is a contiguous subarray and for a group to be maximumProfitable the middle elements of the subarray should be less than left and right, i.e. the max is left/right element.
Return the count of maximumProfitable stock groups.
For ex: prices[i] = [2,3,2]
Output = 5
"""

import math



def maximumProfitable(arr: list):
    count = 0
    stack = []
    for r in range(len(arr)+1):
        if r == len(arr):
            current = math.inf
        else:
            current = arr[r]
        
        while len(stack) > 0 and arr[stack[-1]] < current:
            j = stack.pop()
            
            if len(stack) == 0:
                l = -1
            else: 
                l = stack[-1]
            
            count += r-j+j-l-1
        
        stack.append(r)
    
    return count
    
    
assert(maximumProfitable([2, 3, 2]) == 5)
assert(maximumProfitable([1, 100, 1, 7, 7]) == 11)
