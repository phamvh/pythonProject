class Solution:
    """
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number c
    ould represent. Return the answer in any order.

    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to
    any letters.

    Example 1:

    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    Example 2:

    Input: digits = ""
    Output: []
    Example 3:

    Input: digits = "2"
    Output: ["a","b","c"]
    """
    def phoneToLettersIterative(self, digits: str) -> list[str]:
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result: list[list[str]] = []
        for c in mapping[digits[0]]:
            result.append([c]) # each is a list of a single letter

        for i in range(1, len(digits)):
            letters = mapping[digits[i]]
            updated_result: list[list[str]] = []
            for c in letters:
                for lis in result:
                    copy = lis[::]
                    copy.append(c) # or lis.copy().append(c), and note that this method returns None; it just modifies a list
                    updated_result.append(copy)
            result = updated_result

        result = ["".join(li) for li in result]
        return result

    def __phoneToLettersBackTrackRecursive(self, digits: str,
                                           curr: int, # current index in the digits being processed
                                           prev_state: list[str],
                                           mapping: dict[str, str],
                                           result: list[str] # store the final result
                                           ) -> None:
        """
        Use backtracking technique here. Refer to file back_tracking.py for details about backtracking algo.
        Remember, this is a DFS, so a state is just the path to the current node in a tree. It's ONE SINGLE val, not multiple.
        In this case, it is just a list of letters from the root to the current node.
        """
        # if leaf is reached
        if curr == len(digits):
            result.append("".join(prev_state))
            return # go back the prev state

        digit = digits[curr]
        letters = mapping[digit]
        for c in letters:
            prev_state.append(c)
            self.__phoneToLettersBackTrackRecursive(digits, curr + 1, prev_state, mapping, result)

            ## now back track to the prev state to process the next letter c in letters
            prev_state.pop() # remove the last letter that was added in the deeper state just prior to this

    def phoneToLettersBackTrackRecursive(self, digits: str) -> list[str]:
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        curr = 0
        prev_state = [] # start from the root, so the path is empty
        result = []
        self.__phoneToLettersBackTrackRecursive(digits, curr, prev_state, mapping, result)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.phoneToLettersIterative("23"))
    print(sol.phoneToLettersBackTrackRecursive("23"))
