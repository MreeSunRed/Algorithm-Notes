# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def inorder(root, height):
            if root == None:return height
            left = inorder(root.left, height + 1)
            right = inorder(root.right, height + 1)
            return max(left, right)
        return inorder(root, 0)
