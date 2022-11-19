"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff_list = []
        
        for i in range(len(prices)):
            
            for k in range(i+1, len(prices)):
                if prices[i] < prices[k]:
                    diff_list.append(prices[k] - prices[i])
                
                
                
        if len(diff_list) != 0:
            return sorted(diff_list)[-1]
        else:
            return 0
        
        
        
        
print(Solution().maxProfit([7,6,4,3,1]))

print(float('inf'))