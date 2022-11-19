"""
Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        zero = nums.count(0)  
        
        for i in range(zero):
            nums.remove(0)
            nums.append(0)
            
        return nums
        
print(Solution().moveZeroes([0,1,0,3,12]))