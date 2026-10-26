class MinStack(object):

    class Node:
        def __init__(self, val=None, mins=None):
            self.val = val
            self.mins = mins

    def __init__(self):
        self.stack = []
        self.node = MinStack.Node()
        self.node.mins = 2**31 - 1

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.stack:
            t = MinStack.Node(val=value, mins=value)
            self.stack.append(t)
            return
        top = self.stack[-1]
        t = MinStack.Node(val=value, mins=value)
        if t.mins > top.mins:
            t.mins = top.mins
        self.stack.append(t)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop().val

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1].val

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1].mins
