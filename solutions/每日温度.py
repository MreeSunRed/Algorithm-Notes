class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        s = []
        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                j = s.pop()
                res[j] = i - j
            s.append(i)
        return res
