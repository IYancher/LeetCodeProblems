"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)[::-1]
        
        if x.count("-") == 1:
            x = -int(x.replace("-", ""))
        else:
            x = int(x)
            
        return x if (x > -2**31 and x < 2**31-1) else 0
        
        
        
        
print(Solution().reverse(-130))