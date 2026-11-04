class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0] + heights + [0]
        s = []
        maxH = 0
        for i, v in enumerate(heights):
            while s and heights[s[-1]] > v:
                height = heights[s.pop()]
                width = i - s[-1] - 1
                temp = height * width
                maxH = max(maxH, temp)
            s.append(i)
        return maxH
