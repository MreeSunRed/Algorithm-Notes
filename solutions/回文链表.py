# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
        for i, val in enumerate(nums):
            if val != nums[-1 * (i + 1)]:
                return False
            if i >= len(nums) / 2:
                return True
        return True
