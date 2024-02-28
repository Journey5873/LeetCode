class Solution(object):
    def maxArea(self, height):

        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            wall_height = height[left] if height[left] < height[right] else height[right]

            area = wall_height * (right - left)
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area