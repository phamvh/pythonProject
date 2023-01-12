if __name__ == '__main__':
    """
    To convert to a built-in data type, simply use the type name as function, like:
    int("3")
    int(2)
    float(2.2)
    int(2.2)
    """

    print(int(1))  # 1
    print(int(1.1))  # 1
    print(int("3"))  # 3
    # print(int("3.3")) # -->> error: invalid literal for int

    #print(long("4")) -->> long() is not defined though

    print(float(1))
    print(float(1.1))
    print(float("2"))
    print(float("2.2"))

    print(str(1))
    print(str(1.1))
    print(str(2.2))

    # eval() takes a string, and evaluates it as a python statement
    # it is like a compiler that compile a string of code into executable code
    x = eval("print(5)")
    x # since it is a statement, we can call that statement by calling x

    x = eval("2 + 2")
    print(x) # now x is an expression, not a full statement, so it becomes a var.

    x = eval("x * 2") # 4 * 2 = 8
    print(x)

    # eval("5 + 7 -")  -->> error because the string is not a valid python code fragment

    print(complex(1,2)) # (1+2j)

    # repr(x) is similar to toString in Java. It converts an object into a representable string.
    d = {1: "one", 2: "two"}
    s = repr(d)
    print(s) # {1: 'one', 2: 'two'}

    print(tuple((1,2,3))) # (1, 2, 3)  Notice parens?
    print(list((1,2,3)))  # [1, 2, 3] See? square brackets, not parens
    x = dict(((1, "one"), (2, "two"))) # dict() accepts a sequence of tuples of size 2 as (key, val)
    print(x) # {1: 'one', 2: 'two'}

    print(chr(98)) # 'b'  converts an int to a char
    print(ord('b')) # 98 converts a single char to int

