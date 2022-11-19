"""
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        set_num = set(nums)
        
        for i in set_num:
            if nums.count(i) == 1:
                return i
        
        
                


print(Solution().singleNumber([7,6,4,3,1,6,7,3,1]))