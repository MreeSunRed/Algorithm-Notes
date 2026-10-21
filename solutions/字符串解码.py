class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                temp = []
                while stack[-1] != '[':
                    temp.append(stack.pop())
                stack.pop()
                num = []
                while stack != [] and stack[-1].isdigit():
                    num.append(stack.pop())
                num = num[::-1]
                mul = 0
                for i in num:
                    mul = mul * 10 + int(i)
                temp = temp * mul
                while temp != []:
                    stack.append(temp.pop())
        return "".join(x for x in stack)
