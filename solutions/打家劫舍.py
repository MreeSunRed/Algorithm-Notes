class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        if n == 0:
            return nums[0]
        if n == 1:
            return max(nums[0], nums[1])
        nums[2] = nums[2] + nums[0]
        for i in range(3, len(nums)):
            nums[i] = nums[i] + max(nums[i - 2], nums[i - 3])
        return max(nums[-1], nums[-2])
