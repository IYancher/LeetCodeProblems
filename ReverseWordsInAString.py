"""
Given a string s, reverse the order of characters in each word 
within a sentence while still preserving whitespace and initial word order.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        list = s.split(" ")
        res = ''
        
        for i in range(len(list)):
            list[i] = list[i][::-1]
            res += list[i] + ' '
        
            
        return res.strip()
        
print(Solution().reverseWords("Let's take LeetCode contest"))   