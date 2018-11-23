#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#Input: "Hello" Output: "hello"

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join([i.lower() for i in str])
