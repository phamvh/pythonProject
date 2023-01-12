class Solution:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    26. Remove Duplicates from Sorted Array

    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

    Custom Judge:

    The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
    If all assertions pass, then your solution will be accepted.



    Example 1:

    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    Example 2:

    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    """
    def removeDuplicates(self, arr: list[int]) -> int:
        """
        THis is done in place, so the array will be modified
        The returned val is just the number of unique elements remaining after removal

        Idea: similar to the Dutch flag problem:
        1. Maintain a border, the left of which are all sorted and unique
        2. maintain a curr pointing at the currently processed index:
           if arr[curr] <= arr[border]:
               keep advancing curr, keep border the same
           else:
               swap elements at border + 1 with element at curr
               advance both curr and border
        """
        if not arr or len(arr) <= 1:
            return 0
        border = 0
        curr = 1
        while curr < len(arr):
            if arr[border] < arr[curr]:
                temp = arr[border + 1]
                arr[border + 1] = arr[curr]
                arr[curr] = temp

                curr += 1
                border += 1
            else:
                curr += 1
        return border + 1




if __name__ == '__main__':
    arr = [1,1,2,3,3,4,5,5,6]
    sol = Solution()
    print(sol.removeDuplicates(arr)) # 6
    print(arr) # [1, 2, 3, 4, 5, 6, 3, 5, 1]
