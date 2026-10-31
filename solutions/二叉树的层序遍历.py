from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TNode(object):
    def __init__(self, val=0, left=None, right=None, height=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = height


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        def copy(root1, h):
            if not root1:
                return None
            self.maxh = max(self.maxh, h)
            root2 = TNode(val=root1.val, height=h)
            root2.left = copy(root1.left, h + 1)
            root2.right = copy(root1.right, h + 1)
            return root2

        self.maxh = 0
        root2 = copy(root, 1)
        q = deque()
        q.append(root2)
        res = [[] for _ in range(self.maxh)]
        while q:
            p = q.popleft()
            if not p:
                continue
            res[p.height - 1].append(p.val)

            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        return res
