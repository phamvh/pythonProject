class Solution:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
    """
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # the sort fuction takes a keyword arg as a function to return a key to sort on.
        strs.sort(key=len) # just sort strs based on their length
        min_str = strs[0]  # or, simply min_str = min(strs, key = len) without needing to sort the array. O(n)
        min_len = len(min_str)
        i = min_len
        while i > 0:
            prefix = min_str[0:i]
            common = True
            for s in strs:
                if not s.startswith(prefix):
                    common = False
                    break
            if common:
                return prefix
            else:
                i -= 1
        return ""

    def longestCommonPrefix2(self, strs: list[str]) -> str:
        strs = sorted(strs, key=len) # same as sort() function of str
        result = ''
        # after sorting, we only need to compare the first and the last elements of strs
        # because they differ the most from each other
        min_len = len(strs[0])
        for i in range(min_len):
            if strs[0][i] == strs[-1][i]: # compare the i-th char of the first and the last strings in the sorted array
                result += strs[0][i]
            else:
                break
        return result

if __name__ == '__main__':
    strs: list[str] = ["flower","flow","flight"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))
    print(sol.longestCommonPrefix2(strs))

