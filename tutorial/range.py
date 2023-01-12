if __name__ == '__main__':
    for i in range(4):
        print(i, end=", ") # 0, 1, 2, 3,

    print()
    for i in range(1, 4):
        print(i, end=", ") # 1, 2, 3,

    print()
    for i in range(1,4,2):
        print(i, end=", ") # 1, 3,

    for c in "hello":
        print(c)

    lis = [1,2,3]
    copy = lis[::]
    copy.append("hello")
    print(lis)
    print(copy)