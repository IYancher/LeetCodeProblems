"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ""

        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                string += s[i].lower()
                
        if string == string[::-1]:
            return True
        else:
            return False
        
print(Solution().isPalindrome("0P"))