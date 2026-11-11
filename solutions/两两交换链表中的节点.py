# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def swap(node):
            if node == None or node.next == None:
                return node
            second = node.next
            t = second.next
            second.next = node
            node.next = swap(t)
            return second

        return swap(head)
