class Solution:
    """
    https://leetcode.com/problems/valid-parentheses/
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    Example 1:

    Input: s = "()"
    Output: true
    Example 2:

    Input: s = "()[]{}"
    Output: true
    Example 3:

    Input: s = "(]"
    Output: false
    """
    def isValid(self, s: str) -> bool:
        opens: set[str] = {'(', '[', '{'}
        closes: set[str] = {')', ']', '}'}
        pairs = {"()", "[]", "{}"}
        lis: list[str] = list(s)  # a list of chars
        i = 0
        while len(lis) > 0:
            open = lis[i]
            if open not in opens:
                return False;
            if i + 1 >= len(lis):
                return False
            if (lis[i + 1] in opens):
                i += 1
                continue
            close = lis[i + 1]  # must be a close due to the if-continue above
            if (open + close) in pairs:
                del lis[i + 1]
                del lis[i]
                i = max([0, i - 1])
            else:
                return False
        return True

    def isValid2(self, s):
        """
        This is a way more elegant solution using a stack.
        Remember, every time when you need to remember the last seen item in a loop, then use stack as it's first in last out.
        If you need a queue (efficient first in first out), use deque: queue = deque()
        """
        pairs: dict[str, str] = {'(':')', '[':']', '{':'}'}
        stack: list[str] = []  # use list as a stack.
        i = 0
        for c in s:
            if c in pairs: # one of the openings
                stack.append(c)
            else: # one of the closings
                if len(stack) == 0:
                    return False # no opening to match the closing
                prev = stack.pop() # get and remove the last item from stack
                if pairs[prev] != c:
                    return False
        return stack == []



if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("()"))  # True
    print(sol.isValid("()[]{}()()[]"))  # True
    print(sol.isValid("([{}])")) # True
    print(sol.isValid("([)]")) # False
    print(sol.isValid("({)}"))  # False
    print(sol.isValid("([][]({}))")) # True
    print(sol.isValid("([][]({})]")) # False

    print()
    print(sol.isValid2("()"))  # True
    print(sol.isValid2("()[]{}()()[]"))  # True
    print(sol.isValid2("([{}])"))  # True
    print(sol.isValid2("([)]"))  # False
    print(sol.isValid2("({)}"))  # False
    print(sol.isValid2("([][]({}))"))  # True
    print(sol.isValid2("([][]({})]"))  # False
