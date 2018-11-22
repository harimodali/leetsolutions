#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example
#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

class Solution(object):
    #Sorted list input
    def twoSumSorted(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        
        while start < end:
            csum = nums[start] + nums[end]
            if csum == target:
                return [start,end]
            elif csum < target:
                start +=1
            else:
                end -=1
        return False
    
    #Unsorted list input
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        complements = {}
        for index in range(len(nums)):
            cur = nums[index]
            if cur in complements:
                return [complements.get(cur),index]
            else:
                complements[target-cur] = index
        return False
