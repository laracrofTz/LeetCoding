# Given array of strings strs, group the anagrams together
# Ans can be returned in any order

# What kind of characters do the strings contain?
# Length of the strings in the strs arr, and length of strs?

# sort the letters of each word
# traverse through the array, for eachword, sort it and check if it exists in the dict
# If it doesnt, add the sorted word into the dict as a key, and append the current value 

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = defaultdict(list)
        for i in strs:
            sorted_str = ''.join(sorted(i))
            anagram[sorted_str].append(i)
        return anagram.values()        

