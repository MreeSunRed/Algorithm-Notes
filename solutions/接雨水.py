class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack_height = []
        rain = 0
        for i, v in enumerate(height):
            while stack_height and height[stack_height[-1]] <= height[i]:
                bottom = stack_height.pop()
                if not stack_height:
                    break

                rain += (
                    (min(height[stack_height[-1]], height[i]) - height[bottom])
                    * (i - stack_height[-1] - 1)
                )
            stack_height.append(i)

        return rain
