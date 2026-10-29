# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = head
        last = head
        while first != None:
            first = first.next
            if first == None:
                return None
            first = first.next
            last = last.next
            if last == None:
                return None
            if last == first:
                break
        if first == None:
            return None
        res = head
        while res != last:
            res = res.next
            last = last.next
        return res
