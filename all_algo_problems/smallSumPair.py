# 2 int arrays sorted in non decreasing order
# int k, which is the num of pairs
# A pair consists of a num from arr 1 and num from arr 2
# Return k pairs with the smallest sum

# What are the lengths of the arrays?
# will nums1 and nums2 be the same length?
# Can the arrays consist of negative numbers?
# How large can k be?

from heapq import heappush, heappop # maintains heap invariant so we dont have to heapify again
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(nums1)
        m = len(nums2)
        res = []
        visited = set() # to store the pairs that have alrdy been visited
        minHeap = []
        minHeap.append((nums1[0]+nums2[0], 0, 0)) # sum, index from nums1, index from nums2)
        visited.add((0,0))

        while k>0 and minHeap:
            # pop from minheap
            total, i, j = heappop(minHeap)
            res.append([nums1[i], nums2[j]])

            if i+1<n and (i+1,j) not in visited:
                visited.add((i+1,j))
                heappush(minHeap, [nums1[i+1]+nums2[j], i+1, j])
            if j+1<m and (i,j+1) not in visited:
                visited.add((i,j+1))
                heappush(minHeap, [nums1[i]+nums2[j+1], i, j+1])
            k -= 1
        return res

# Space complexity --> heap data structure can have up to m*n pairs stored, result will have k pairs, O(min(k, mn))
# time complexity --> O(klogk)