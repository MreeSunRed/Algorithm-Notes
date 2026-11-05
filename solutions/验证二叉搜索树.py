# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def bsf(root, low, high):
            if not root:
                return True
            if low is not None and root.val <= low:
                return False
            if high is not None and root.val >= high:
                return False
            return bsf(root.left, low, root.val) and bsf(root.right, root.val, high)

        return bsf(root, None, None)
