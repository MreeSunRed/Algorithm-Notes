# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.plusList(l1, l2, 0)

    def plusList(self, l1, l2, add):
        if not l1 and not l2:
            return None if add == 0 else ListNode(val=add)
        if not l1:
            plusNum = l2.val + add
            l2 = l2.next
        elif not l2:
            plusNum = l1.val + add
            l1 = l1.next
        else:
            plusNum = l1.val + l2.val + add
            l1 = l1.next
            l2 = l2.next
        addnum = 0
        if plusNum >= 10:
            plusNum -= 10
            addnum = 1
        res = ListNode(val=plusNum)
        res.next = self.plusList(l1, l2, addnum)
        return res
