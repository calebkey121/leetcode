"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""

from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [1,null,2,3]
def createTree(nodeList: List[ TreeNode ]) -> TreeNode:
    childrenDistance = 1
    for i in range(len(nodeList)):
        if i == 0 and nodeList[i]:
            
            root = 


class Solution(object):
    def inorderTraversalRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        rlist = []
        if root.left:
            rlist.extend(self.inorderTraversal(root.left))
        rlist.append(root.val)
        if root.right:
            rlist.extend(self.inorderTraversal(root.right))
        return rlist

    def inorderTraversalIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        rlist = []

        stack = [ root ]
        curr = root
        visited = [ root ]
        while stack:
            if curr.left and not in visited:
                curr = curr.left
                stack.append(curr)
                visited.append(curr)


                
            if curr.right and not in visited:
                curr = curr.right
                stack.append(curr)
            else
                stack.pop()
                if stack:
                    curr = stack[-1]

        return rlist