#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.

class Stack(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.insert(0,item)
        
    def pop(self):
        try:
            return self.items.pop(0)
        except IndexError:
            raise IndexError("The stack is empty")
            
    def peek(self):
        return self.items[0]
    
        
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opn = "({["
        clse = ")}]"
        
        for close in clse:
            if s.startswith(close): return False
        
        sstack = Stack()
        balanced = 1
        
        for i in range(len(s)):
            cur = s[i]
            if cur in opn:
                sstack.push(cur)
            elif cur in clse:
                if sstack.isEmpty():
                    return False
                elif clse.index(cur) != opn.index(sstack.pop()):
                    return False
                
        if not sstack.isEmpty():
            return False
        
        return True
