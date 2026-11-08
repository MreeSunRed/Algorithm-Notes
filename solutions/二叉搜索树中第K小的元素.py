# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.k = k
        self.min_k = root.val

        def dsf(root):
            if root is None:
                return
            if self.k == 0:
                return
            dsf(root.left)
            if self.k > 1:
                self.k -= 1
            elif self.k == 1:
                self.k -= 1
                self.min_k = root.val
                return
            dsf(root.right)

        dsf(root)
        return self.min_k
