import time
from typing import List


class Solution:
    """
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    Input:
        nums = [1,2,3,4,5,6,7], k = 3
    Output:
        [5,6,7,1,2,3,4]
    Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


solution = Solution()


if __name__ == '__main__':
    s01 = time.time()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution.rotate(nums, k)
    s02 = time.time()
    print(s02 - s01)
    print(nums)