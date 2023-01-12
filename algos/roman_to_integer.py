class Solution:
    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.



    Example 1:

    Input: s = "III"
    Output: 3
    Explanation: III = 3.
    Example 2:

    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
    Example 3:

    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    def romanToInt(self, s: str) -> int:
        # store the mapping in two dicts, one for a single letter, another for double letters
        singles: dict[str, int] = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        doubles: dict[str, int] = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        result: int = 0
        index = 0
        length = len(s)
        while index < length:
            if index < length - 1:
                # try to get two letters
                two_letters = s[index] + s[index + 1]
                if two_letters in doubles:
                    result += doubles[two_letters]
                    index += 2
                else:
                    # try to get one letter
                    letter = s[index]
                    result += singles[letter]
                    index += 1
            else: # only called when one letter left
                # try to get one letter
                letter = s[index]
                result += singles[letter]
                index += 1

        return result

    def romanToInt2(self, s: str) -> int:
        # only need single letter
        singles: dict[str, int] = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # replace all the double letters with the equivalent single letters
        roman = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX")
        roman = roman.replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        result: int = 0
        for c in roman:
            result += singles[c]

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("MCMXCIV"))

    print(sol.romanToInt2("MCMXCIV"))

