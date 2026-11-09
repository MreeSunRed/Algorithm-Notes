class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 3)
        dp[2] = 2
        dp[1] = 1
        i = 3
        while i <= n:
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1
        return dp[n]
