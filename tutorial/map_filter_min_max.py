if __name__ == '__main__':
    """
    similar to map and filter in Java stream.
    map(fun, iter)
    filter(fun, iter)
    """
    lis = [1,2,3,4,5]
    # pass a lambda as a function here, it returns a map object, which needs to be converted to a list
    mapped_obj = map(lambda x: x*x, lis)
    print(mapped_obj) # <map object at 0x10fb67ee0>
    # need to convert to a list
    square_lis = list(mapped_obj)
    print(square_lis) # [1, 4, 9, 16, 25]

    filtered = filter(lambda x: x > 2, lis)
    print(filtered) # <filter object at 0x10f6dfe50>
    # still need to convert to a list
    print(list(filtered)) # [3, 4, 5]

    print(min(lis)) # 1
    print(max(lis)) # 5
    # provide a key function, which returns a key to compare upon
    print(min(lis, key=lambda x: 5 - x)) # 5
