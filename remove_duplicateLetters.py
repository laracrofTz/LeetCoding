# Given string s, remove duplicate letters, so that every letter only appears once
# Ensure the result is in smallest lexiographical order
    # What is lexicographical order?
    # The order is determined first by length of string and then alphabetical order
    # In this question the alphabetical order matters since the length of all the resultant string possibilities will be the same
    # So for example: Input --> "cbacdcbc"
    # output possibilities --> 'cbad', 'cadb', 'bacd', 'acdb' ... etc
    # The possibilities have to be compared lexicographically

# Possible clarifications
    # Will the input string contain special characters, punctuation, digits? --> No
    # Will the input be a mixture of uppercase/lowercase or only specifically one category?
        # Only lowercase letters
    # How long can the input string be?

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or s.islower() != True or s.isalpha() != True:
            raise Exception("Empty input")

        visited = set() # stores the characters that have been visited previously
        stack = [] 
        last_occurence = {} # stores the index of the last occurence of the character

        for i in range(len(s)):
            last_occurence[s[i]] = i

        for i in range(len(s)):
            if s[i] not in visited: # checks if current character has not been visited --> meaning its not in the stack
                while len(stack) != 0 and stack[-1] > s[i] and last_occurence[stack[-1]] > i: # checks if topmost element in stack is larger than current char and if last occurence of topmost char is larger than curr char index
                    visited.remove(stack.pop()) # removes the popped char from visited set
                stack.append(s[i])
                visited.add(s[i])
        return ''.join(stack)

# Time complexity --> O(n^2) 
# Space complexity --> Best case is O(1), worst case is O(26) due to 26 possible letters

# My misunderstanding
# I thought I could just get the result after stack operations and permutate them to get the lexicographical order
# However, the duplicate characters can be removed from any index, its not restricted to be removed from right to left