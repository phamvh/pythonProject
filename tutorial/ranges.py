if __name__ == '__main__':
    """
    range() is an in-built function which returns a sequence starting from 0 , incrementing by 1, till a specified number
    range(start, stop, step)
       start is optional, default to 0
       stop is required
       step is the number to increment, optional, default to 1
    """
    for i in range(5): # start from 0 by default
        print(i, end=", ") # 0, 1, 2, 3, 4,

    print()
    for i in range(1,5): # start from 1
        print(i, end=", ") # 1, 2, 3, 4,

    print()
    for i in range(1,5,2): # start from 1, step = 2
        print(i, end=", ") # 1, 3,

