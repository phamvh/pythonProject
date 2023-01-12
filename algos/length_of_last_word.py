class Solution:
    """
    https://leetcode.com/problems/length-of-last-word/
    Find the length of the last word
    """

    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        i = l - 1
        count = 0
        word_seen = False
        while i >= 0:
            if s[i] != " ":
                count += 1
                i -= 1
                word_seen = True
            else:
                if word_seen:
                    break
                else:
                    i -= 1
        return count

    def lengthOfLastWord2(self, s: str) -> int:
        words = s.split() # when no separator given, space is used, and empty words are discarded in result
        last = words[-1] # return last
        return len(last)

    def lengthOfLastWord3(self, s: str) -> int:
        """
        this would not work correctly, because the result includes a string consisting of empty space.
        To make it work correctly, need to strip spaces from both ends first.

        """
        words = s.strip().split(' ')
        last = words[-1] # return last
        return len(last)

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))
    print(sol.lengthOfLastWord("luffy is still joyboy"))

    print(sol.lengthOfLastWord2("Hello World"))
    print(sol.lengthOfLastWord2("   fly me   to   the moon  "))
    print(sol.lengthOfLastWord2("luffy is still joyboy"))

    print(sol.lengthOfLastWord3("Hello World"))
    print(sol.lengthOfLastWord3("   fly me   to   the moon  "))
    print(sol.lengthOfLastWord3("luffy is still joyboy"))

