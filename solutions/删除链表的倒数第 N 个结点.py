# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        list_len = 0
        list1 = head
        while list1 != None:
            list1 = list1.next
            list_len += 1
        target = list_len - n + 1
        last = head
        pre = last.next
        count = 2
        if target == 1:
            return head.next
        while count != target:
            pre = pre.next
            last = last.next
            count += 1
        last.next = pre.next
        return head
