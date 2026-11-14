class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h_list = sorted(set(height))
        area_max = 0
        for i in h_list[::-1]:
            left = 0
            while height[left] < i:
                left += 1
            right = len(height) - 1
            while height[right] < i:
                right -= 1
            area_max = max(area_max, i * (right - left))
        return area_max
