from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)

        left, right, maximum_area = 0, length - 1, 0

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)

            maximum_area = max(maximum_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum_area
