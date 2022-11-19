"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Given a roman numeral, convert it to an integer.
    
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        roman_nums = []
        
        i = 0
        while i < len(s) - 1:
            if s[i] + s[i+1] in roman.keys():
                roman_nums.append(roman.get(s[i] + s[i+1]))
                i += 2
            else:
                roman_nums.append(roman.get(s[i]))
                i += 1
        try:        
            if s[-2] + s[-1] not in roman.keys():      
                roman_nums.append(roman.get(s[-1]))
        except IndexError:
            roman_nums.append(roman.get(s[-1]))
        
        res = 0    
        for k in range(len(roman_nums)):
            res += roman_nums[k]
                
        return res
                
        
print(Solution().romanToInt("MCMXCIV"))