# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = dict()
        l = head
        while l != None:
            if l in s:
                return True
            s[l] = True
            l = l.next
        return False
