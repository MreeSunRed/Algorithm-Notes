class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        s = []
        max_len = 0
        for k in num_set:
            if k - 1 not in num_set:
                count = 0
                while k + count in num_set:
                    count += 1
                max_len = max(max_len, count)
        return max_len
