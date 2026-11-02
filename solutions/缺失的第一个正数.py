class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        res = 1
        for i in range(0, len(nums)):
            if nums[i] <= 0:
                continue
            d[nums[i]] = True
            while res in d:
                res = res + 1
        return res
