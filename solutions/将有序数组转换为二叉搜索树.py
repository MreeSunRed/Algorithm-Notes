# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def ToBST(left, right):
            if left > right:
                return None
            half = (left + right) // 2
            root = TreeNode(val=nums[half])
            root.left = ToBST(left, half - 1)
            root.right = ToBST(half + 1, right)
            return root

        return ToBST(0, len(nums) - 1)
