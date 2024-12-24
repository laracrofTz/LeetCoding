# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# MY SOLUTION with Time complexity of O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            remainder = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==remainder:
                    res.append(i)
                    res.append(j)
                    return res
                
# SOLUTION from LEETCODE with Time complexity of O(n)
    def twoSum_optimised(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []

# This solution makes use of a dictionary to store the values of the array each time hence making it easier to access index with the key value
# Referring to example 1, we store 2 inside the dictionary in the first iteration. 
# In 2nd iteration we check if target - nums[1] is found in the dictionary, and it is since it was added in the previous iteration.
# Returns list with the indices accessed using the key value.