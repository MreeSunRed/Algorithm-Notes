class Solution(object):
    def calculateScore(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        s1 = 0
        s2 = 0
        while a != 0:
            if a % 2 == 1:
                s1 += 1
            a = int(a / 2)
        while b != 0:
            if b % 2 == 1:
                s2 += 1
            b = int(b / 2)
        if s1 >= s2:
            return s1 * s2
        return int(s2 / s1)
