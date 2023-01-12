if __name__ == '__main__':
    """
    while expression:
        statements
    """
    i = 0
    while i < 10:
        print(i, end=", ")
        i += 1     # note, there is no ++ in python



    # while else
    print()
    i = 1
    while i < 2:
        print(i, end=", ")
        i += 1
    else:
        print("now i >= 2")
        print("indeed, i =", i)


    i  = 1
    while i != 1: print("i is not 1") # one line if the suite has one statement only


    """
    for loop has this syntax:
    
    for iterating_var in sequence:
        statements
    """
    fruits = ["banana", "apple", "melon"]
    for fruit in fruits:
        print(fruit)

    # use index
    for index in range(len(fruits)):
        print("fruit at index", index, "is", fruits[index])


    # for else: else is executed when the loop has exhausted its iterations.
    print()
    for fruit in fruits:
        print(fruit, end=", ")
    else:
        print()
        print("No more fruits")


    # break and continue
    for i in range(10):
        if i == 4: break
        if i % 2 == 0: continue
        print(i, end=", ")  # will print: 1, 3,


    # pass statement
    """
    pass is used as a placeholder for future code.
    when pass is executed, nothing happens, but you avoid getting an error where empty code is not allowed.
    For example, empty code is not allowed in loops.
    
    Also, just notice that pass is used to make something similar to interface in Java, meaning when one defines
    a function, he can just put pass in it, and no implementation yet. See the print() function, for example.
    """
    for i in range(10):
        pass  # future code go here. Without pass, an error would occur due to empty code.