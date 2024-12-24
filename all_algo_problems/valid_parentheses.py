# Given string containing just the characters: (, ), {, }, [, ] 
# String is only valid if the open bracket is closed by the same corresponding closed bracket and
# the brackets must be open and closed in the correct order
# Clarifications:
    # The string only consists of the parenthesis characters? Not any other characters?
        # Yes only the different parenthesis
    # What is the maximum length of the string?
        # 10^4
    # Can the string start with a closed bracket?
        # If it can start with a closed bracket, it is not a valid input string, since it violates the order of the brackets

# Possible corner, edge cases would be
# Null string, string with no parentheses, string with just whitespaces

# using stack data structure
from queue import LifoQueue

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        self.s = s

        if len(self.s) == 0:
            return False
        
        # initialise a new stack
        p_stack  = LifoQueue()

        for c in self.s:
            if c in parentheses.keys():
                p_stack.put(c)
            elif c in parentheses.values():
                # check if the stack is empty
                if p_stack.empty() == True:
                    return False
                elif c != parentheses[p_stack.get()]:
                    return False
            else:
                return False
        if p_stack.qsize() != 0: # if p stack is not empty, means the brackets were not properly closed
            return False
        return True
                
s1 = Solution()
print(s1.isValid("()"))
print(s1.isValid("()[]{}"))
print(s1.isValid("(])"))
print(s1.isValid("(]"))
print(s1.isValid(""))
print(s1.isValid("  "))
print(s1.isValid("["))

# Time complexity: O(n) due to the traversal with for loop
# Space complexity: 
# Average --> O(k), where is k is the maximum difference between number of closing and opening brackets
# Worst --> O(n), where n is the size of input string, eg. s = "(((((((((((({{{{{[[[", the stack keeps growing
# Best --> O(1), where input string just contains closing brackets, or could be an empty string, or could contain no parentheses