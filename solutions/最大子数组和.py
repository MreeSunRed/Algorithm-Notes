class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum=nums[0]
        tempmax=nums[0]
        for i in range(1,len(nums)):
            tempmax=max(nums[i],nums[i]+tempmax)
            maxnum=max(tempmax,maxnum)
        return maxnum
        