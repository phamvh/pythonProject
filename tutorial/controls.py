if __name__ == '__main__':
    """
    if expression:
        statements
    """

    i = 1
    if i == 1:
        print("one")
    if (i == 1): # use parens when needed
        print("one")

    if i:  # 1 evaluates to True.
        print(i)


    if i == 2:
        print("two")
    else:  # colon needed just like for the if.
        print("not two")


    if i == 2:
        print("two")
    elif i == 0:
        print("zero")
    else:
        print("not 2 and not 0")


    # single statement suites
    # if the if suite has one statement only, then the statement can go on the same line where the if is.
    if i == 1: print(i)