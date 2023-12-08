# Given a root of the binary tree, construct a string consisting of parenthesis and integers from binary tree with preorder traversal way and return it
# Omit all empty parenthesis 
# preorder traversal --> visit root first, then traverse left subtree, once done traverse right subtree --> like depth first search

# Input is a Tree node --> the root node
# Output is a string

# Possible clarifications
# I am assuming for ever node I visit, there will be an open bracket
# Can the node values be negative?
# How large can each node value be?
# How large can the tree be?

# Test cases
# If root node is empty --> then return empty string
# If only root node exists --> return the value parsed as string 
# If left node does not exist, doesnt mean right node doesnt exist!

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root.val == 0:
            return ""
        
        res = str(root.val)

        if root.left:
            res += "(" + self.tree2str(root.left) + ")" 
        if root.right:
            if not root.left:
                res += "()"
            res += "(" + self.tree2str(root.right) + ")" 
        
        return res


# Complexity
# Time --> Since we are traversing through the tree and visiting each node, it will be O(n)
# Space --> Number of recursive calls depend on the height of the tree, but the output depends on the number of nodes travelled, so O(n)?