#Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different. In other words, it measures the minimum number of substitutions required to change one string into the other, or the minimum number of errors that could have transformed one string into the other.

#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#Given two integers x and y, calculate the Hamming distance.
#Note:
#0 ≤ x, y < 231

#Hamming distance between 1 (0 0 0 1) and 4 (0 1 0 0) is 2. They differ in 2 bits
#Input: x = 1, y = 4 Output: 2

#Solution: Use Binary x ^ y and count the number of 1's in the result

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #Use X ^ Y
        return bin(x ^ y).count('1')

