def printSpiralMatrix(rows: int, cols: int) -> None:
    """
    Given the size of a matrix, print the elements in the matrix in a spiral order:
    first, left to right, down, right to left, up.
    Each time the travel sees an already visited cell, it changes the direction clockwise.
    Example: the following matrix has its elements increasingly ordered in the spiral order.

    0 , 1 , 2
    7 , 8 , 3
    6 , 5 , 4

    """
    if not rows or not cols:
        return
    row, col = 0, 0
    pre_row, pre_col,  = 0, -1
    #visited: list[list[bool]] = [[False for c in range(cols)] for r in range(rows)]
    #visited[0][0] = True
    spiral: list[list] = [[0 for c in range(cols)] for r in range(rows)]
    spiral[0][0] = 1
    count = 1
    while True:
        if col > pre_col:
            if col + 1 <= cols - 1 and not spiral[row][col + 1]:
                count += 1
                pre_col = col
                col += 1
                #visited[row][col] = True
                spiral[row][col] = count
            else: # top right corner
                if row + 1 <= rows - 1 and not spiral[row + 1][col]:
                    count += 1
                    pre_col = col
                    pre_row = row
                    row += 1
                    #visited[row][col] = True
                    spiral[row][col] = count
                else:
                    break

        elif col < pre_col:
            if col - 1 >= 0 and not spiral[row][col - 1]:
                count += 1
                pre_col = col
                col -= 1
                #visited[row][col] = True
                spiral[row][col] = count
            else: # bottom left corner
                if row - 1 >= 0 and not spiral[row - 1][col]:
                    count += 1
                    pre_col = col
                    pre_row = row
                    row -= 1
                    #visited[row][col] = True
                    spiral[row][col] = count
                else:
                    break
        elif row > pre_row:
            if row + 1 <= rows - 1 and not spiral[row + 1][col]:
                count += 1
                pre_row = row
                row += 1
                #visited[row][col] = True
                spiral[row][col] = count
            else: # bottom right corner
                if col - 1 >= 0 and not spiral[row][col - 1]:
                    count += 1
                    pre_row = row
                    pre_col = col
                    col -= 1
                    #visited[row][col] = True
                    spiral[row][col] = count
                else:
                    break
        else: # row < pre_row
            if row - 1 >= 0 and not spiral[row - 1][col]:
                count += 1
                pre_row = row
                row -= 1
                #visited[row][col] = True
                spiral[row][col] = count
            else: # top left corner
                if col + 1 <= cols - 1 and not spiral[row][col + 1]:
                    count += 1
                    pre_row = row
                    pre_col = col
                    col += 1
                    #visited[row][col] = True
                    spiral[row][col] = count
                else:
                    break

    for r in spiral:
        for c in r:
            print(c, end=" , ")
        print()

def printSpiralMatrix2(rows: int, cols: int) -> None:
    """
    Same as the function above, but the algo looks much cleaner.
    The main idea is that we move clockwise, so we have a periodic change of indices row and col as follows:
    changes = ((0, 1), (1, 0), (0, -1), (-1, 0))
    where:
    changes[0] = (0,1) indicates that rows remains the same, and col inrements by 1
    changes[1] = (1, 0) indicates that row increments by 1 while col remains the same
    etc.
    When changes[0] finishes, we should advance to changes[1], and then changes[2] and then changes[3],
    and back to changes[0] again
    """
    row, col = 0, 0
    spiral: list[list[int]] = [[0 for c in range(cols)] for r in range(rows)]
    changes = ((0, 1), (1, 0), (0, -1), (-1, 0))
    p = 0 # initial period. It can be 0, 1, 2 or 3
    count = 1
    while True:
        if row in range(rows) and col in range(cols) and not spiral[row][col]:
            spiral[row][col] = count
            count += 1
            row = row + changes[p][0]
            col = col + changes[p][1]
        else:
            # undo the last change of indices. This is important
            row = row - changes[p][0]
            col = col - changes[p][1]
            p += 1 # make a turn clockwise
            if p > 3:
                p = 0 # complete one round, go back to 0
            row = row + changes[p][0]
            col = col + changes[p][1]
            if  row not in range(rows) or col not in range(cols) or spiral[row][col]:
                break # finish

    for r in spiral:
        for c in r:
            print(c, end=" , ")
        print()

if __name__ == '__main__':
    printSpiralMatrix(3,3)
    print()
    print(printSpiralMatrix2(3, 3))






