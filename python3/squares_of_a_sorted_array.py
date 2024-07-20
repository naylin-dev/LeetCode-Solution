from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_len: int = len(nums)
        result: List[int] = [0] * nums_len

        L: int = 0
        R: int = nums_len - 1

        index: int = nums_len - 1

        # Two pointers technique, one from the left and one from the right
        while L <= R:
            left: int = nums[L] * nums[L]
            right: int = nums[R] * nums[R]

            # If the left is greater than the right, put the left to the result
            if left > right:
                result[index] = left
                L += 1
            # Otherwise, put the right to the result
            else:
                result[index] = right
                R -= 1
            index -= 1

        return result
