class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d1 = dict()
        for i, v in enumerate(nums):
            if v not in d1:
                d1[v] = 0
        s = []
        for k in d1:
            if k - 1 not in d1:
                s.append(k)
        maxn = 0
        for i in s:
            count = 0
            while i + count in d1:
                count += 1
            maxn = max(maxn, count)
        return maxn
