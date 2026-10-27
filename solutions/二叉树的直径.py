# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diag = 0

        def length(root):
            if root == None:
                return 0
            l = length(root.left)
            r = length(root.right)
            d = max(l, r) + 1
            self.diag = max(self.diag, l + r + 1)
            return d

        length(root)
        return self.diag - 1
