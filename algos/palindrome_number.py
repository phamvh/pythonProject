class Solution:
    def isPalindrome(self, num: int) -> bool:
        """
        Given an integer x, return true if x is a
        palindrome
        , and false otherwise.
        """
        s = str(num)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

    def isPalindrome2(self, num: int) -> bool:
        if num < 0:
            return False
        lis: list[int] = []
        while num > 0:
            lis.append(num % 10)
            num = num // 10 # floor division

        i, j = 0, len(lis) - 1
        while i < j:
            if lis[i] != lis[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

    def isPalindrome3(self, num: int) -> bool:
        s = str(num)
        lis: list[str] = list(s) # turn this into a list of int
        reversed_lis: list[str] = reversed(lis)
        # join a string with all elements of an iterable of strings
        # if the iterable is not of type string, need to convert its elems into string first (use comprehension)
        reversed_str = "".join(reversed_lis)
        return s == reversed_str  # note that == is used to compare value, while "is" is used to compare identities


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(-121))
    print(sol.isPalindrome(321))

    print(sol.isPalindrome2(121))
    print(sol.isPalindrome2(-121))
    print(sol.isPalindrome2(321))

    print(sol.isPalindrome3(121))
    print(sol.isPalindrome3(-121))
    print(sol.isPalindrome3(321))