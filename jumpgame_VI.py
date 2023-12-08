# Given a 0 indexed int array (the index of first element is 0) called nums, and integer k
# Initially I am standing at index 0. In one move I can jump at most k steps forward without going outside the array
# I can jump from index i (curr position) to any index in the range of [i+1, min(n-1, i+k)] inclusive
# I need to reach the last index of the array.
# The score is the sum of all nums[j], where j is each index I visit
# Return the max score I can get

# Possible clarifications
# What is the length of the array?
# Will the array only consist of + ints? Or can there be - ints too. --> Yes both can exist
# I am assuming since k represents the number of steps to move forward, it cannnot be 0 or -ve? --> Yes range of k is 1 to 10^5

# Possible ideas
# Brute Force
    # Try out all the possible ways to jump from the current index and get the max score
    # This would result in O(k^n) time complexity, since there are k choices at each index
# Use DP with recursion (Top down apporach, memoisation)
    # dp[i] would denote the max score obtained from the index i
    # We can start from n-1 index (last index of array), since we would know what the max score is --> nums[n-1] (since we cannot jump any further)
    # Traverse back through the array and calculate the max score attainable
        # Check if the calculated score exists in the table, else we calculate and add it in
    # However this would still be O(k^n) since we still have to traverse through k^n choices to get the max score
# 

class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
    