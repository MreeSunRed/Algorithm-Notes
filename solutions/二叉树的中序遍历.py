# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        stack = []
        def inorder(root):
            if root == None:return
            inorder(root.left)
            stack.append(root.val)
            inorder(root.right)
            return stack
        inorder(root)
        return stack
