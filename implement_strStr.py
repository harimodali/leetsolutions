#Implement strStr().
#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#Input: haystack = "hello", needle = "ll"
#Output: 2 Explanation: the first instance of occurance happens at index 2

#Input: haystack = "aaaaa", needle = "bba"
#Output: -1

class Solution(object):
#    def strStr(self, haystack, needle):
#        """
#        :type haystack: str
#        :type needle: str
#        :rtype: int
#        """
#        if needle == '':
#            return 0
#        if needle not in haystack:
#            return -1
#        import re
#        return re.search(needle,haystack).span()[0]
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        len1=len(haystack)
        len2=len(needle)
        if len1<len2: 
            return -1
        for i in range(len1-len2+1):
            if haystack[i:i+len2]==needle:
                return i
        return -1
