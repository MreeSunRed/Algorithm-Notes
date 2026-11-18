# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        # pre 中左右[3,9,20,15,7]
        # in 左中右[9,3,15,20,7]
        # [3,9,20,null,null,15,7]
        def build(preorder, inorder):
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            index_in = inorder.index(preorder[0])
            root.left = build(preorder[1 : index_in + 1], inorder[:index_in])
            root.right = build(preorder[index_in + 1 :], inorder[index_in + 1 :])
            return root

        return build(preorder, inorder)
