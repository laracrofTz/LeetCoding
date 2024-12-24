# Given root of a binary tree, return the average values of each level in the tree
# Return the values in an array

# What should the return type of the values be? --> Float
# Is there any specific number of decimal places required in the ans? 
# Can the node have negative numbers --> Yes, range of each node value can be a signed 32 bit int range
# Am I right to say that if a root node doesnt have a left node it can still have a right node?

# Possible test cases
# Tree might have only one level, only root exists

# Can use BFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        q = []

        # append the root node into the queue
        q.append(root)
        while len(q) != 0:
            total = 0
            count = len(q)
            for i in range(len(q)):
                curr = q.pop(0)
                total += curr.val
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
            res.append(total/count)
            print(total/count)
        return res
    
r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
s = Solution()
print(s.averageOfLevels(r))


# Complexity
# Time complexity is O(n) since I am only traversing the tree once, where n is the number of nodes
# Space complexity is dependent on the number of levels or height, so O(h)