class Solution:
    """
    https://leetcode.com/problems/add-binary/
    Given two binary strings a and b, return their sum as a binary string.

    Example 1:

    Input: a = "11", b = "1"
    Output: "100"
    Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"
    """

    def add_two_bits(self, c1: str, c2: str, carry: str) -> tuple[str, str]:
        """
        Given two bits and a carry (from the prev addition), return the result bit and the new carry
        Example:
             (0,0,1) -> return (1,0)
             (1,0,1) -> return (0,1)
         """
        match (c1, c2):
            case ('0', '0'):
                if carry == '0':
                    return ('0', '0')
                else:
                    return ('1', '0')
            case ('0', '1') | ('1', '0'):
                if carry == '1':
                    return ('0', '1')
                else:
                    return ('1', '0')
            case _:  # ('1', '1') _ is used for default
                if carry == '1':
                    return ('1', '1')
                else:
                    return ('0', '1')

    def addBinary(self, a: str, b: str) -> str:
        if None in (a, b):
            return a or b
        stack1 = list(a)
        stack2 = list(b)
        i,j = len(stack1) - 1, len(stack2) - 1
        res: list[int] = []
        carry = '0'
        while stack1 and stack2:
            (c1, c2) = (stack1.pop(), stack2.pop())
            (result_bit, carry) = self.add_two_bits(c1, c2, carry)
            res.append(result_bit)
        remaining = stack1 or stack2
        while remaining:
            if carry == '0':
                res.append(remaining.pop())
            else:
                c = remaining.pop()
                (result_bit, carry) = self.add_two_bits(c, '0', carry)
                res.append(result_bit)
        if carry == '1':
            res.append(carry)

        res.reverse()
        return "".join(res)

if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary("01", "10"))

    print(ord('b'))

