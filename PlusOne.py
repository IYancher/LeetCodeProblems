"""
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
                
        res = ''
        for i in range(len(digits)):
                        
            res += str(digits[i])
        
        return list(map(int, str(int(res) + 1)))
        
        
        
print(Solution().plusOne([1,2,3]))