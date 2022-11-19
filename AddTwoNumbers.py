"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        a = ''
        b = ''
        for i in l1[::-1]:
            a += str(i)
        for i in l2[::-1]:
            b += str(i)
        res = int(a) + int(b)
        return list(str(res))[::-1]
        
solution = Solution()

print(solution.addTwoNumbers([2,4,3], [5,6,4]))