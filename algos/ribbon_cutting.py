"""
You are given an array of integers a, where each element a[i] represents the length of a ribbon.

Your goal is to obtain k ribbons of the same length, by cutting the ribbons into as many pieces as you want.

Your task is to calculate the maximum integer length L for which it is possible to obtain at least k ribbons of length L by cutting the given ones.

Example

For a = [5, 2, 7, 4, 9] and k = 5, the output should be solution(a, k) = 4.

example

Here's a way to achieve 5 ribbons of length 4:

Cut the ribbon of length 5 into one ribbon of length 1 (which can be discarded) and one ribbon of length 4.
Cut the ribbon of length 7 into one ribbon of length 3 (which can be discarded) and one ribbon of length 4.
Use the existing ribbon of length 4 (no need to cut it)
Cut the ribbon of length 9 into two ribbons of length 4 (and one of length 1 which can be discarded)
Discard the ribbon of length 2.
And since it wouldn't be possible to make 5 ribbons of any greater length, the answer is 4.

For a = [1, 2, 3, 4, 9] and k = 6, the output should be solution(a, k) = 2.

Here's one way we could make 6 ribbons of length 2:

Cut the ribbon of length 9 into four ribbons of length 2 and one ribbon of length 1 (which won't be used).
Cut the ribbon of length 4 into two ribbons of length 2.
Ignore all other ribbons (1, 2, and 3). Even though ribbons with lengths 2 and 3 can also be used to obtain the ribbon of length 2, we don't need more than 6 ribbons of that length.
It would technically be possible to make 6 ribbons of a length as great as 2.25, but since only integer values are allowed, the answer is 2.

a: [5, 2, 7, 4, 9]
k: 5
Expected Output:
4

Input:
a: [1, 2, 3, 4, 9]
k: 6
Expected Output:
2

Input:
a: [1, 2, 3, 4, 9]
k: 5
Expected Output:
3


Input:
a: [8, 4, 2, 6, 1, 2, 1, 7]
k: 14
Expected Output:
2

Input:
a: [4, 8, 4, 5, 3, 7, 1, 2, 6]
k: 5
Expected Output:
4


"""


def ribbons(num, size):
    return num // size


def solution(a, k):
    if not a:
        return 0
    m = max(a)
    l = 0
    for size in range(1, m):
        count = 0
        for n in a:
            count += ribbons(n, size)
            if count >= k:
                l = size
    return l
