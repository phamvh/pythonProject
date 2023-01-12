if __name__ == '__main__':
    """
    So far, arrays in pyhthon are the same as lists, as far as I know.
    Here, arrays are discussed: https://www.w3schools.com/python/python_arrays.asp
    but when I run type of an array, the result is list. 
    """

    lis = []
    #lis[2] = 2 # will throw an error: index out of range

    # to fix this issue:
    lis = [None]*5 # or [0]*5
    lis[0] = 0
    lis[2] = 2
    lis[4] = 4
    print(lis) # [0, None, 2, None, 4]
