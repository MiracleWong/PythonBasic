#!/usr/bin/env python
#  -*- coding:utf-8 -*-

def binary_search(mylist, item):
    low = 0
    high = len(mylist) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = mylist[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

mylist = [1, 3, 5, 7, 9, 11, 23]
print(binary_search(mylist, 23))


class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums, target):
        # write your code here
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = int((low + high) / 2)
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
        return None