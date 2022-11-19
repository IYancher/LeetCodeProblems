"""
Given a string s, find the length of the longest substring
without repeating characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        str_len = []
        
        for i in range(len(s)):
            str = []
            str.append(s[i])
            for k in range(i+1, len(s)):
                if s[k] in str:
                    break
                else:
                    str.append(s[k])
            str_len.append(len(str))
            
        
        try:
            return sorted(str_len)[-1]
        except IndexError:
            return 0
        
        
print(Solution().lengthOfLongestSubstring(""))