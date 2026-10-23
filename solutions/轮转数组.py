from collections import deque
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        q = deque(nums)
        for i in range(k%len(nums)):
            t = q.pop()

            q.appendleft(t)
        nums[:] = q
