# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        s = []

        def preorder(root):
            if root == None:
                return
            # visit
            s.append(root)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        if s == []:
            return
        root = s.pop()
        while s != []:
            cur_node = s.pop()
            cur_node.left = None
            cur_node.right = root
            root = cur_node
