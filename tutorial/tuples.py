if __name__ == '__main__':
    """
    tuples are like lists, but READ_ONLY lists. No changes allowed.
    They are ordered, meaning you can use index to access their elements
    tuples use parens (), while lists use brackets []
    
    Note: comparison of python collections:
    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.

    """
    tuple1 = (1,2,3,"four")
    tuple2 = ("five", 6)
    print(tuple1)
    print(tuple1[3])
    print(tuple1[1:3]) # sub-tuple, from 1st to 3rd, including 1st, excluding 3rd
    print(tuple1[1:])  # sub-tuple from 1st till the end
    print(tuple1 * 2) # create a NEW tuple that doubles the old one
    print(tuple1 + tuple2) # create a new tuple that concatenate two tuples
    print(tuple1.index(2)) # get the first index of a value
    print(tuple1.count(3)) # count the number of occurrences of  value
    print(len(tuple1))

    # convert a tuple into a list
    list1 = list(tuple1)
    print(list1) # [1, 2, 3, 'four']  notice the square brackets

    # convert a list to a tuple
    t = tuple(list1)
    print(t)  # (1, 2, 3, 'four') notice the parens

    # seems in Python2, to create a tuple of a single value, you need to provide a comma,
    # even though it's one element
    single = (1,)
    print(single)

    # any sequence declared without using parens, brackets or braces is defaulted to be a tuple
    # for this reason, parens are optional when declaring a tuple because it ises the default mode
    # lists, however, need brackets []
    t = 1,2,3,4,5
    print(t)  # (1, 2, 3, 4, 5)
    print(type(t))  # <class 'tuple'>