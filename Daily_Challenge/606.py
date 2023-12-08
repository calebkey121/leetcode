# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        returnString = str(root.val)

        # While you have a left, open , call on left, close 
        if root.left:
          left = self.tree2str(root.left)
          returnString += '('
          returnString += left
          returnString += ')'
        elif root.right: # if right is populated they want blank here
          returnString += "()"
        # While you have a right, open, call right, close
        if root.right:
          right = self.tree2str(root.right)
          returnString += '('
          returnString += right
          returnString += ')'

        return returnString
