# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        first = head
        second = head.next
        while second and second.next:
            first = first.next
            second = second.next.next
        mid = first.next
        first.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.Merge(left, right)

    def Merge(self, root1, root2):
        res = ListNode(0)
        ls = res
        while root1 and root2:
            if root1.val <= root2.val:
                res.next = root1
                root1 = root1.next
                res = res.next
            else:
                res.next = root2
                root2 = root2.next
                res = res.next
        if root1:
            res.next = root1
        else:
            res.next = root2
        return ls.next
