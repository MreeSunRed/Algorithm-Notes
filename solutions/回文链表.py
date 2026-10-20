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
        nums = 0
        hnode = head
        while hnode != None:
            hnode = hnode.next
            nums+=1
        i=0
        midnode = head
        while i< nums/2:
            midnode = midnode.next
            i+=1
        tailA = None
        while midnode != None:
            p = midnode
            midnode = midnode.next
            p.next = tailA
            tailA = p
        midnode=tailA
        while midnode != None:
            if midnode.val != head.val:
                return False
            midnode=midnode.next
            head=head.next
        return True
            

