#Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.
#(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

#Input: L = 10, R = 15
#Output: 5
#Explanation:
#10 -> 1010 (2 set bits, 2 is prime)
#11 -> 1011 (3 set bits, 3 is prime)
#12 -> 1100 (2 set bits, 2 is prime)
#13 -> 1101 (3 set bits, 3 is prime)
#14 -> 1110 (3 set bits, 3 is prime)
#15 -> 1111 (4 set bits, 4 is not prime)

class Solution(object):
    
    def is_prime(self, num):
        if num < 2:
            return False
        else:
            for i in range(2,num):
                if num % i == 0:
                    return False
        return True
    
    def get_bit_count(self, num):
        
        return bin(num).count('1')
    
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        for n in range(L,R+1):
            if self.is_prime(self.get_bit_count(n)):
                count += 1
        return count
