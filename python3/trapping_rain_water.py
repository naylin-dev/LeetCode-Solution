from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        # If the list has less than 3 elements, there is no water that can be trapped
        if length < 3:
            return 0

        trapped_water = 0

        # Find the highest point in the list
        highest_point = height.index(max(height))

        # Calculate the trapped water on the left side
        left = height[0]
        for i in range(highest_point):
            left = max(left, height[i])
            trapped_water += left - height[i]

        # Calculate the trapped water on the right side
        right = height[length - 1]
        for i in range(length - 2, highest_point, -1):
            right = max(right, height[i])
            trapped_water += right - height[i]

        return trapped_water
