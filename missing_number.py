#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#Input: [9,6,4,2,3,5,7,0,1]  Output: 8
#Input: [0] Output: 1;  Input: [1] Output: 0

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        maximum = max(nums)
        
        n = maximum - minimum + 1
        
        diff = (n * (maximum + minimum)/2) - sum(nums)
        if diff == 0:
            if minimum == 1:
                return 0
            else:
                return maximum + 1
        return diff
