class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        left = nums[0]
        for i in range(1, len(nums)):
            res[i] *= left
            left *= nums[i]
        right = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
