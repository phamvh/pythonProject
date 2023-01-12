from typing import List, Dict


class Solution:
    def getFrequencies(self, nums: list[int]) -> dict[int, List[int]]:
        """
         # make the freqquency hash table
        """
        # when initiate a var to an empty val, give it type so you can get code suggestion later, such as append()
        f: dict[int, list[int]] = {}
        for i, val in enumerate(nums): # enumerate() helps get both index and value of an enumeratable obj.
            if val in f:
                f[val].append(i)  # just append i to the list. Note that this append method returns None
            else:
                f[val] = [i]  # create a new list
        return f

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/
        Given an array of integers nums and an integer target, return indices of the two numbers such that they a
        dd up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.
        """
        if (nums is None) | (len(nums) == 0): # note that precedence of "is" is not high in Python. Parens needed
            return []

        f = self.getFrequencies(nums)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in f:
                for j in f[diff]:
                    if i != j:
                        return [i, j]


    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        """
        this solution is copied from leetcode
        """
        d = {}
        # enumerate() helps getting both index and value
        for i, val in enumerate(nums): # i is index, starting from 0, val is the value from nums
            diff = target - val
            if diff in d:
                return [d[diff], i]
            d[val] = i

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3], 6))

    print(sol.twoSum2([2, 7, 11, 15], 9))
    print(sol.twoSum2([3, 2, 4], 6))
    print(sol.twoSum2([3, 3], 6))

    ### some tests with enumerates()
    nums = ["John", "Mike", "Kit", "Hue"]
    e = enumerate(nums)
    print(e) # <enumerate object at 0x10cc69d80>
    print(type(e)) # <class 'enumerate'>
    # feed e to list() function to get a list
    print(list(e)) # [(0, 'John'), (1, 'Mike'), (2, 'Kit'), (3, 'Hue')], see? both index and value: a list of tuples of index and val.
