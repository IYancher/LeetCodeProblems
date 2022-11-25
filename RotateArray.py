"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example :

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k <= len(nums):
            a = len(nums) - k
        else:
            a = len(nums) - (k - len(nums))
            
        nums[:] = nums[a:] + nums[:a]
        print(a)
        print(nums)
        
        
        
Solution().rotate([1,2,3], 4)