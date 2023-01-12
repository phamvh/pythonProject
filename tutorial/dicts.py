if __name__ == '__main__':
    """
    This is like a hash table
    key can be any type, but usually string or number
    value can be any type
    dict use {}
    
    Notes:
    when duplicate keys are encountered during assignments, the last assignment wins, like in Java
    Keys must be immutable, like string, numbers, tuples, but cannot be a list
    """
    dict1 = {0 : "zero", "three" : 3} # keys can be of different types
    dict1[1] = "one"
    dict1["two"] = 2
    dict2 = {5 : "five"}

    print(dict1)
    print(dict1[1]) # get a value with square brackets surrounding a key
    print(dict1["two"])

    keySet = dict1.keys() # return a set of keys, don't know about python set yet
    print(keySet) # dict_keys([0, 'three', 1, 'two'])
    values = dict1.values() # returns values, which looks like a list because of square brackets
    print(values) # dict_values(['zero', 3, 'one', 2])

    print(dict1.get(1)) # get a value given key
    print(dict1.get("apple"))  # None, because such key does not exist
    print(dict1.get("apple", "Tim Cook"))  # "Tim Cook" is the default value to be returned if key "apple" does not exist

    print(dict1.pop(1)) # get and remove a value given key
    dict1[1] = "one" # added back the popped one
    print("dict1 is", dict1)
    del dict1[1] # you can also delete an element by its key by using del operator
    print(dict1)
    dict1[1] = "one"  # added back the deleted one

    items = dict1.items() # return a set of items, like Map.Entry in Java
    print(items) # dict_items([(0, 'zero'), ('three', 3), ('two', 2), (1, 'one')])
    for item in items:
        print(item, end=",  ") # (0, 'zero')
        print(type(item)) # this is a tuple
        print(item[0]) # 0
        print(item[1])           # "zero"
        break

    print(dict1.popitem()) # remove and return the LAST added item (like a stack)
    dict1[1] = "one" # added it back

    # print(dict1[8]) this will cause an error cuz key 8 does not exist
    # check if a key exists in a dict
    print(1 in dict1)  # True
    print(8 in dict1)  # False
    if 8 in dict1:
        print("this won't execute")

    # this is similar to get,
    # but if key does not exist, then it sets dict1[10] = "ten" in the dict, and return "ten"
    print(dict1.setdefault(10, "ten")) # 10 does not exist in keys, so it set 10 to "ten"
    print(dict1.get(10)) # now 10 is in the key, so get() should return "ten"


    # clear and delete
    dict1.clear() # clear all content of dict1, but dict1 still exists, it's just empty
    print(dict1) # {}
    del dict1  # delete the whole thing, so dict1 no longer exists
    # print(dict1)  --> NameError: name 'dict1' is not defined.
    # create dict1 back
    dict1 = {0 : "zero", "three" : 3}

    # key must be of immutable type: string, numbers, tuples, but not list nor set
    # trying to add a list as a key
    list1 = ["apple"]
    #dict1[list1] = "Tim Cook"  # -->> TypeError: unhashable type: 'list'

    # Update a dict by adding all values from another dict
    dict1.update({"apple" : "Tim Cook", "tesla" : "Elon Musk", 0 : "ZERO"})  # "ZERO" will be new value instead of "zero"
    print(dict1) # {0: 'ZERO', 'three': 3, 'apple': 'Tim Cook', 'tesla': 'Elon Musk'}

