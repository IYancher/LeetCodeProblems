"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        if target < nums[0]:
            return 0
        
        if target > nums[-1]:
            return len(nums)
        
        k = 0
        while target > nums[k]:
            k += 1
            continue
        return k
                
        
        
print(Solution().searchInsert([1,3,5,6], 7))