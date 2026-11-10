class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first0 = 0
        after0 = 1
        n = len(nums)
        while after0 <= n - 1 or first0 <= n - 1:
            while after0 <= n - 1:
                if nums[after0] != 0 and nums[after0 - 1] == 0:
                    break
                after0 += 1
            while first0 <= n - 1 and nums[first0] != 0:
                first0 += 1
            if after0 > n - 1 or first0 > n - 1:
                break
            if nums[first0] == 0 and nums[after0] != 0:
                t = nums[first0]
                nums[first0] = nums[after0]
                nums[after0] = t
