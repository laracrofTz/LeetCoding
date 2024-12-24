# Given 2 strings, ransomNote and magazine, return true if ransomNote can be constructed by the letters in magazine
# The letters in magazine can only be used once to construct the ransom note

# What is the length of the input strings? --> cannot be empty, ransomNote can go up to infinite, magazine can be 10^5
# What kind of characters do the input strings consist of? --> only lowercase characters

# Ransom note cannot be constructed if the frequency of characters in magazine is lesser than that in ransomNote --> so this is what we have to check for
# As long as the ransom note length is more than the magazine, then immediately return false, since ransom note can never be constructed

from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # check if len of note is more than magazine length, return false
        if len(ransomNote) > len(magazine): return False

        r_hashmap = Counter(ransomNote)
        m_hashmap = Counter(magazine)

        # if the letters in ransomNote are more than the letters in magazine, note cannot be constructed
        for k, v in r_hashmap.items():
            if v > m_hashmap[k]:
                return False
        
        # if we are able to traverse the hashmaps fully, then it means ransom note can be constructed using magazine
        return True
    
# Complexity
# Time complexity --> O(n) since we are traversing the hashmap
# Space complexity --> let k be the number of unique characters across ransom note and magazine, k would never be more than 26. O(k)