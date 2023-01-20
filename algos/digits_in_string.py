"""
 Problem:: Take an input string parameter and determine: For all pairs of digits where there are exactly 3 question marks
 between them, do all pairings add up to 10.
     strings = [("arrb6???4xxbl5???eee5", True),
     ("acc?7??sss?3rr1??????5", True),
     ("5??aaaaaaaaaaaaaaaaaaa?5?5", True),
     ("9???1???9???1???9", True),
     ("aa6?9", False),
     ("8???2???9", False),
     ("10???0???10", False),
     ("aa3??oiuqwer?7???2", False)]
"""
def evaluate(s: str) -> bool:
    if not s or len(s) == 0:
        return False
    first_index = -1
    encounted = False
    anypair = False
    count = 0
    for i in range(0, len(s)):
        if s[i].isdigit():
            if not encounted:
                encounted = True
                first_index = i
                count = 0
            else:
                if count == 3:
                    sum = int(s[first_index]) + int(s[i])
                    if sum != 10:
                        return False
                    else:
                        first_index = i
                        count = 0
                        anypair = True
                else:
                    first_index = i
                    count = 0
        elif s[i] == "?":
            count += 1
    return anypair

if __name__ == '__main__':
    inputs = [("arrb6???4xxbl5???eee5", True),
     ("acc?7??sss?3rr1??????5", True),
     ("5??aaaaaaaaaaaaaaaaaaa?5?5", True),
     ("9???1???9???1???9", True),
     ("aa6?9", False),
     ("8???2???9", False),
     ("10???0???10", False),
     ("aa3??oiuqwer?7???2", False)]
    for input in inputs:
        print(evaluate(input[0]))

