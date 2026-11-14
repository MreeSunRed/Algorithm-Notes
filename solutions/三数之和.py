from collections import Counter


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        num_hash = dict(Counter(nums))
        if len(num_hash) == 1:
            if nums[0] == 0:
                return [[0, 0, 0]]
        left = 0
        res = []
        while left < len(nums) - 2 and nums[left] <= 0:
            right = len(nums) - 1
            while left < right - 1 and nums[left] * nums[right] <= 0:
                target = -1 * (nums[left] + nums[right])
                if target in num_hash:
                    if target == nums[left] and num_hash[target] < 2:
                        right -= 1
                        continue
                    if target == nums[right] and num_hash[target] < 2:
                        right -= 1
                        continue
                    res.append(sorted([nums[left], target, nums[right]]))
                right -= 1
            left += 1

        return [list(x) for x in {tuple(x) for x in res}]
