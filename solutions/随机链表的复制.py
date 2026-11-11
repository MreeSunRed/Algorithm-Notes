# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        old = head
        copyhead = Node(0)
        new = copyhead
        node_map = {}
        while old is not None:
            new_node = Node(x=old.val, random=old.random)
            new.next = new_node
            new = new_node
            node_map[old] = new_node
            old = old.next
        copyhead = copyhead.next
        new = copyhead
        while new is not None:
            if new.random is not None:
                new.random = node_map[new.random]
            else:
                new.random = None
            new = new.next
        return copyhead
