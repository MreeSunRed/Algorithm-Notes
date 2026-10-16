# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s=set()
        nodea=headA
        nodeb=headB
        while nodea!= None:
            s.add(nodea)
            nodea=nodea.next
        while nodeb!= None:
            if nodeb in s:
                return nodeb
            nodeb=nodeb.next
        return None