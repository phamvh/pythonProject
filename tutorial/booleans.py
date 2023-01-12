if __name__ == '__main__':
    a = True;
    print(a)
    print(type(a)) # <class 'bool'>

    a = 2
    b = 4
    print(a == b)

    # one can use the bool() function to evaluate an expression to a boolean value
    print(bool(a != b)) # in this case it is redundant to use bool()
    print(bool(a)) # here, bool() evaluate an existing number to True
    print(bool(-2)) # still true
    c = None
    print(bool(c)) # False, cuz c is None
    d = 0
    print(bool(d)) # also False


