# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:

# -231 <= x <= 231 - 1

# PYTHON SOLUTION --> I DONT LIKE RECURSION
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse_str_x = str(x)[::-1] # use list slicing to reverse string, recall slicing syntax: list[start:stop:step]
        if str(x) == reverse_str_x:
            return True
        else:
            return False  

# ANOTHER SOLUTION without parsing to string
    def isPalindrome_wihtoutconversion(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False #negative value will automatically return false
        
        inputNum = x
        newNum = 0
        while x > 0:
            newNum = newNum * 10 + x % 10
            x = x // 10
        return newNum == inputNum