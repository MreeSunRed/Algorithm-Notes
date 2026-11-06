import sys


class Solution(object):
    def minMergedInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        macsh = sys.maxsize
        i = 0
        while i < len(nums) - 1:
            a = str(nums[i])
            b = str(nums[i + 1])
            c = int(a + b)
            i += 2
            macsh = min(macsh, c)
        return macsh
