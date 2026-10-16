class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        keyv=dict()
        for i,num in enumerate(nums):
            if target-num in keyv:
                return [i,keyv[target-num]]
            keyv[num]=i