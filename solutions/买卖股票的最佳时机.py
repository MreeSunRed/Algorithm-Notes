class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxNum = 0
        flag = False
        minNum = prices[0]
        for i in range(1, len(prices)):
            if minNum > prices[i]:minNum = prices[i]
            if (prices[i] - minNum) > maxNum:
                flag = True
                maxNum = prices[i] - minNum
        if flag:
            return maxNum
        return 0
