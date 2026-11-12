class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # s[i][j]=s[i-1][j-1]+s[i-1][j]
        if numRows == 1:
            return [[1]]
        res = [[1]]
        for i in range(2, numRows + 1):
            pre = [0] + res[i - 2] + [0]
            cur = [pre[j] + pre[j + 1] for j in range(i)]
            res.append(cur)

        return res
