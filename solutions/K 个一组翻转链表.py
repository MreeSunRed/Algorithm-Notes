# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        def reserveK(root, k):
            tail = root
            count = k
            while tail != None and count > 1:
                tail = tail.next
                count -= 1
            if count > 1 or tail == None:
                return root
            after_node = tail.next
            head = None
            tail_root = root
            head_tail = tail
            count = k
            while count > 0:
                p = root
                root = root.next
                p.next = head
                head = p
                count -= 1
            tail_root.next = reserveK(after_node, k)
            return head_tail

        return reserveK(head, k)
