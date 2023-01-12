class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        https://leetcode.com/problems/longest-substring-without-repeating-characters/
        Longest Substring Without Repeating Characters

        Use the Sliding Window approach here. O(n)
        """
        if not s:
            return 0
        ## Note: you CANNOT do window = {}. as python will treat it as a dict, not a set.
        # so either use set() to get an empty set, or window = {s[0]} to tell Python this is a set
        window: set[str] = set() # store chars from low to high - 1
        low, high, max_len = 0, 0, 0 # low = beginning of window inclusive, high = end of window exclusive
        while high < len(s):
            c = s[high]
            if c not in window:
                window.add(c)
                high += 1
                if max_len < len(window):
                    max_len = len(window)
            else:
                window.discard(s[low]) # use discard, don't use remove()
                low += 1
        return max_len


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb")) # 3
    print(sol.lengthOfLongestSubstring("bbbbb")) # 1
    print(sol.lengthOfLongestSubstring("pwwkew")) # 3

