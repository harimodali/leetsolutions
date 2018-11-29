#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

#Example 1:
#Input: 121
#Output: true

#Example 2:
#Input: -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

#Example 3:
#Input: 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.#

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        final = 0
        orig = x
        while orig !=0:
            final = final * 10 + orig % 10
            orig //=10
        
        if final != x:
            return False
        else:
            return True
