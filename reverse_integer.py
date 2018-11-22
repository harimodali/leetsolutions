class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        max_num = (math.pow(2,32)-1)/2
        multiplier = 1
        return_val = 0
        
        if x < 0:
            multiplier = -1
            x *= -1
        while x != 0:
            return_val = return_val * 10 + x % 10
            if return_val > max_num:
                return 0
            x /=10
        return return_val * multiplier
