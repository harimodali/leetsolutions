#Write a function that takes a string as input and returns the string reversed.
#Input: "hello" Output: "olleh"
#Input: "A man, a plan, a canal: Panama"
#Output: "amanaP :lanac a ,nalp a ,nam A"

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s)
        start = 0
        end = len(s)-1
        
        while start < end:
            tmp = slist[start]
            slist[start] = slist[end]
            slist[end] = tmp
            start += 1
            end -=1
        
        return ''.join(slist)

    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s)
        slist.reverse()
        return ''.join(slist)

    def reverseString3(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(reversed(s))

    def reverseString4(self,s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1] 
