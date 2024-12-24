# Given string s, find the first non repeating character in it and return its index
# If does not exist, return -1

# Possible clarifications
# What does the input string contain? Digits? Special characters? etc --> only consists of lowercase letters
# What is the max or min length of the string?
# I am assuming the string is read from left to right direction, sequentially.

from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s.islower() == False or s.isalpha() == False:
            raise Exception('Invalid input')

        charFreq = Counter(s) # can take in str, list, dictionar, key mapping (eg. a=2, b=3...) as args
        # returns dictionary with frequency values
        
        for i in range(len(s)):
            if charFreq[s[i]] == 1:
                return i
            
        return -1
        