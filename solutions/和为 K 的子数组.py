class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = dict()
        count = 0  # prefix
        res = 0
        for i in range(len(nums)):
            count += nums[i]
            target = count - k
            if target == 0:
                res += 1
            res += dic.get(target, 0)
            if count not in dic:
                dic[count] = 1
            else:
                dic[count] += 1
        return res
