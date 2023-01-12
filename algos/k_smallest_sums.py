import heapq
from typing import List

"""
    https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
    You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

    Define a pair (u, v) which consists of one element from the first array and one element from the second array.

    Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

    Example 1:

    Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
    Output: [[1,2],[1,4],[1,6]]
    Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
"""


def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    """
    The idea of this algo is as follows:
    Imagine a matrix of size n*m (n = len(nums1), m = len(nums2), where element at (i,j) = nums1[i] + nums2[j]
    Easy to see that on the same row, any elements on the right are >= on the left, cuz same nums[i], while nums2 are sorted in increasing order.
    Similarly, on the same column, elements are also increasing.

    So create a heap, put nums1[0] + nums2[0] in it.
    Each time we pop (i,j) from the heap, simply add the (i+1, j) and (i, j+1) to the heap as those are the next two smallest.
    We need to pop the heap k times, and each time we only add max 2 elements, so size of heap is ~ 2k.
    Complexity is therefore O(k log k).

    Note about heap in Python: heap does not allow a key function to compare like in Java, but Python recommend to compute
    the value of comparison right away, and put it as first element in a tuple, and add the tuple to the heap.
    """
    if not nums1 or not nums2 or not k:
        return []

    result: list[list[int]] = []
    count = 0
    lis = [(nums1[0] + nums2[0], 0, 0)]
    used = set((0,0))
    while count < k and lis:
        smallest = heapq.heappop(lis)
        i = smallest[1]
        j = smallest[2]
        result.append([nums1[i], nums2[j]])
        count += 1
        if i < len(nums1) - 1:
            if (i+1, j) not in used:
                used.add((i+1,j))
                heapq.heappush(lis, (nums1[i + 1] + nums2[j], i + 1, j))
        if j < len(nums2) - 1:
            if (i, j+1) not in used:
                used.add((i,j+1))
                heapq.heappush(lis, (nums1[i] + nums2[j + 1], i, j + 1))
    return result


def kSmallestPairs_WRONG(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    """
    This does not work correctly.
    Counter example:
    [-10,-4,0,0,6]
    [3,5,6,7,8,100]
    k = 10
    My output:
    [[-10,3],[-10,5],[-10,6],[-10,7],[-10,8],[-4,3],[0,3],[0,3],[6,3],[-4,5]]
    Correct output from leetcode:
    [[-10,3],[-10,5],[-10,6],[-10,7],[-10,8],[-4,3],[-4,5],[-4,6],[0,3],[0,3]]

    I verified and my theory on the indices was simply wrong.
    """
    if not nums1 or not nums2 or not k:
        return []

    result = [[nums1[0], nums2[0]]]
    count = 1

    left1, right1 = 0, 1  # indices on first array
    left2, right2 = 0, 1  # on second array
    l1, l2 = len(nums1), len(nums2)

    while left1 < l1 and left2 < l2 and count < k:
        if right1 > l1 - 1:
            left2 += 1
            right1 = left1 + 1
            continue
        if right2 > l2 - 1:
            left1 += 1
            right2 = left2 + 1
            continue
        if nums1[left1] + nums2[right2] < nums2[left2] + nums1[right1]:
            result.append([nums1[left1], nums2[right2]])
            print(result[-1])
            right2 += 1
            count += 1
        else:
            result.append([nums1[right1], nums2[left2]])
            print(result[-1])
            right1 += 1
            count += 1

    if count == k:
        return result

    while left1 < l1 and right2 < l2 and count < k:
        result.append([nums1[left1], nums2[right2]])
        right2 += 1
        count += 1

    while left2 < l2 and right1 < l1 and count < k:
        result.append([nums1[right1], nums2[left2]])
        right1 += 1
        count += 1

    return result

if __name__ == '__main__':
    #print(kSmallestPairs([1,7,11],[2,4,6],3)) # [[1, 2], [1, 4], [1, 6]]
    #print(kSmallestPairs([1,1,2], [1,2,3], 2)) # [[1, 1], [1, 1]]
    #print(kSmallestPairs([1,2], [3], 3)) # [[1, 3], [2, 3]]

    print(kSmallestPairs([-10,-4,0,0,6], [3,5,6,7,8,100], 10))
