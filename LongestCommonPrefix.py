"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        
        prefix = ''
        
        
        k = 0
        while True:
            list = []
            try:
                for i in range(len(strs)):
                    list.append(strs[i][k])
                    pass
                k += 1
                
                if len(list) == list.count(list[0]):
                    prefix += list[0]
                else:
                    break
                    
                
            except IndexError:
                break
        
        
                
        return prefix
        
        
        


print(Solution().longestCommonPrefix(["cir","car"]))        