# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        def check(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            return a.val == b.val and check(a.left, b.right) and check(a.right, b.left)
        return check(root, root)
