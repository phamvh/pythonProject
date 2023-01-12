if __name__ == '__main__':
    """
    Do NOT use miltiplication to create 1D or 2D arrays in Python as it creates unexpected behaviors:
    like: 
    arr = [0] * 10
    THis creates an array of length 10, but all of them point to the same int object due to multiplication
    
    See: https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/ 
    """

    # use list comprehension
    arr = [0 for i in range(5)]
    print(arr) # [0, 0, 0, 0, 0]

    # for 2D, use nested loop in list comprehension
    row, col = 5, 4   # this is more like tuple assignment
    ## this is like a nested loop in Java:
    # for(int r ...)
    #    for (int c ...) {
    #        arr[r][c] = 0;
    #    }
    arr = [[0 for c in range(col)] for r in range(row)]
    print(arr) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    ## traditional code. use type for clarity
    arr: list[list[int]] = []
    for i in range(row):
        column: list[int] = []
        for j in range(col):
            column.append(0)
        arr.append(column)
    print(arr)

