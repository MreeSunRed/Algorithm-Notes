# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        l3 = ListNode()
        head = l3
        while l1 and l2:
            if l1.val >= l2.val:
                l3.next = l2
                l2 = l2.next
                l3 = l3.next
                l3.next = None
            else:
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
                l3.next = None
        l3.next = l1 or l2
        head = head.next
        return head

    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if lists == []:
            return None
        while len(lists) > 1:
            i = 0
            while i < len(lists) and i + 1 < len(lists):
                mer_list = self.merge(lists[i], lists[i + 1])
                lists[i] = mer_list
                del lists[i + 1]
                i += 1
        return lists[0]
