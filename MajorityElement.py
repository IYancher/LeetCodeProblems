"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        set_num = set(nums)
        res = 0
        
        for i in set_num:
            if nums.count(i) > len(nums) / 2:
                return i

print(Solution().majorityElement([2,2,1,1,1,2,2]))