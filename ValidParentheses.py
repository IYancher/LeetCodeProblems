"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brackets = ["(", "{", "["]
        close_brackets = [")", "}", "]"]
        for i in range(len(s)):
            for k in range(i+1, len(s)):
                pass
        
        
print(Solution().isValid(""))