# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.res = []

        def dsf(root, h):
            if root == None:
                return
            if h > len(self.res):
                self.res.append(root.val)
            dsf(root.right, h + 1)
            dsf(root.left, h + 1)

        dsf(root, 1)
        return self.res
