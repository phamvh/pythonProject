class BackTracking:
    """
    https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28
    Read more about backtracking above.
    A typical example of backtracking is a permutation problem: Find all permutation of "ABC".
    Backtracking uses recursion and normally DFS. BFS would need too much space complexity.
    The term backtracking means:
      - we go from one state to the next state in DFS, and till the leaf
      - if the leaf is a solution, print it. If not, ignore it
      - backtrack to prev state by one level, and try another state

    In summary:
      - backtracking is a searching technique
      - DFS is an ideal way to implement backtracking
    """
    def __permute(self,
                  s: str,
                  k: int,
                  depth: int,
                  used: dict[str, bool],
                  prev_permutation: list[str],
                  result: list[str]
                  ) -> None:
        """
        :param s: a string of all given letters
        :param k: size of permutation needed
        :param depth: current depth of search state, which is the current size of permutation: 1 till k
        :param used: a dict that show which letters have been used, which have not.
        :param prev_permutation: the permutation of the previous state, or of size (depth - 1). Remember that this is
        DFS so there is only ONE prev permutation, like AB, and C has not been used, so we just need to append C to it.
        :return: all permutations
        """
        """
        Given a set of n letters as a string, find all k-permutations.
        Example: given ABC, and k = 2 then, return: AB, AC, BA, BC, CA, CB.
        To better understand backtracking, think of this problem like printing all path from root to leaf:
        
                    root(empty)
                   /     |     \
                  A      B      C
               /     \
              B        C
              |        |
              C        B  (leaf level)

        In backtracking, we assume that we know the result for one state (depth), we need to find results for the 
        next deeper state depth + 1.
        In here, let's assume that state is depth = 1, 2..., k
        Assume we know the result for depth: list[str], each item is of size "depth"
        Need to find the result for depth + 1 by calling the function recursively. 
        In addition to the main params, like letters and k, fpr recursion we also need to pass:
          - all the letters that have been used
          - depth - current size of permutations
          - prev_permutations: the result of prev state: all permutations of size k
          - result: something to hold the final result whenever the leaf in DFS is reached
          
        Perhaps, the most important and the most confusing thing is the prev state. It is just a SINGLE value.
        It is a DFS, so the previous state is just the path from the root to a node. It is not ALL permutations of 
        the previous depth.  
        """
        # if the leaf is reached, store the result and return to prev state.
        if depth == k:
            result.append("".join(prev_permutation))
            return

        for c in s:
            if not used[c]:
                prev_permutation.append(c)
                used[c] = True
                prev_permutation
                self.__permute(s, k, depth + 1, used, prev_permutation, result)

                # now, after furthering the DFS in the statement above, we need to backtrack to the prev state to run
                # the next character c.
                # specifically, these two vars will be used for the next c in s.
                # Note that the result at the leaf has already been added in line 54.
                print(f"backtracking at depth {depth + 1}")
                used[c] = False
                prev_permutation.remove(c)

    def permute(self, s: str, k: int) -> list[str]:
        if not s or not k:
            return []
        used = {}
        for c in s:
            used[c] = False
        prev_permutation = []
        result = []
        self.__permute(s, k, 0, used, prev_permutation, result)
        return result



    def __phoneToLettersBackTrackRecursive(self, digits: str,
                                           curr: int, # current index in the digits being processed
                                           prev_state: list[str],
                                           mapping: dict[str, str],
                                           result: list[str] # store the final result
                                           ) -> None:
        """
        Use backtracking technique here.
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
            print(f"backtracking at depth {curr}")
            prev_state.pop() # remove the last letter that was added in the deeper state just prior to this

    def phoneToLettersBackTrackRecursive(self, digits: str) -> list[str]:
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
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqr', '8': 'tuv', '9': 'wxyz'}
        curr = 0
        prev_state = [] # start from the root, so the path is empty
        result = []
        self.__phoneToLettersBackTrackRecursive(digits, curr, prev_state, mapping, result)
        return result

if __name__ == '__main__':
    bt = BackTracking()
    print(bt.permute("ABC", 3))

    print(bt.phoneToLettersBackTrackRecursive("23"))










