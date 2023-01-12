from bisect import bisect_left
from math import floor, ceil


class Solution:
    """
    https://leetcode.com/problems/search-insert-position/
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:

    Input: nums = [1,3,5,6], target = 5
    Output: 2
    Example 2:

    Input: nums = [1,3,5,6], target = 2
    Output: 1
    Example 3:

    Input: nums = [1,3,5,6], target = 7
    Output: 4
    """

    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 0:
            return 0
        (low, high) = (0, len(nums) - 1) # this is tuple assignment, can be done without parens
        if target <= nums[low]:
            return 0
        elif nums[high] < target:
            return high + 1
        elif nums[high] == target:
            return high

        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif target < nums[mid]:
                high = mid
            else:
                return mid
        return high


    def searchInsert2(self, nums: list[int], target: int) -> int:
        """
        Python has module bisect for this exact purpose
        https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
        """
        return bisect_left(nums, target, 0, len(nums) - 1)

    def searchInsert3(self, nums: list[int], target: int) -> int:
        """
        This is O(n log n), but it is for learning the index function of a list
        """
        if target in nums:
            return nums.insert(target)
        nums.append(target)
        nums.sort()
        return nums.insert(target)

if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))
    print(sol.searchInsert2([1,3,5,6], 5))
    print((2+3)/2) # 2.5
    print(floor(2.5)) # 2
    print(ceil(2.5))  # 3


