if __name__ == '__main__':
    print(3 ** 2) # 3 to the power of 2

    print(21/10) # 2.1
    print(21 % 10) # 1
    print(21 // 10) # 1  floor division, just division and the result is floored.

    a = True
    b = False
    c = True
    print(a and b) # False
    print(a or b)  # True
    # print(a xor b) xor does not exists in python
    print(not a) # False

    # membership operators: in, not in
    list1 = [1,2,3]
    print(1 in list1) # True
    print(4 in list1) # False
    print(1 not in list1) # False
    print(4 not in list1) # True

    # identity operators: is, is not: compare the identities of two vars, like == in Java
    # in Python, == is used to compare values, not identities
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1]

    print(list1 == list2) # True
    print(list1 is list2) # False
    print(id(list1)) # function id() returns the id of an object
    print(id(list2)) # the id (address?) of list1 is not the same as the id of list 2
    print(list1 is not list2) # True
    print(list1 == list3) # False

