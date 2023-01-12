if __name__ == '__main__':
    """
    Use enumerate() function when you want to get both index and value while looping through a collection
    """
    ### some tests with enumerates()
    nums = ["John", "Mike", "Kit", "Hue"]
    e = enumerate(nums)
    print(e)  # <enumerate object at 0x10cc69d80>
    print(type(e))  # <class 'enumerate'>
    # feed e to list() function to get a list
    print(list(e))  # [(0, 'John'), (1, 'Mike'), (2, 'Kit'), (3, 'Hue')], see? both index and value: a list of tuples of index and val.
