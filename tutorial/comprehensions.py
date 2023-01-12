if __name__ == '__main__':
    """
    list comprehension is like "Stream.map" in Java. It applies a function to every element of a list
    and return a new list (NOT modifying the existing list)
    
    Similar for set and dict
    https://diveintopython3.net/comprehensions.html 
    """
    ########### list comprehension #################
    list1 = [1, 2, 3, 4]
    list2 = [elem * 2 for elem in list1]
    print(list2)  # [2, 4, 6, 8]

    # you can even do filtering by using "if" at the end
    list2 = [elem * 2 for elem in list1 if elem >= 3]
    print(list2) # [6, 8]

    list2 = [elem * 2 for elem in list1 if elem >= 3] # if the expression after if is true, elem is included in the result
    print(list2)  # [6, 8]

    # you can apply list comprehension to a dict or any sequence, return a list or even a dict, and vice versa
    dict1 = {"one" : 1, "two": 2, "three" : 3}
    key_list = [f for f in dict1]  # still list comprehension, but for a dict
    value_list = [dict1.get(f) for f in dict1]
    print(key_list) # ['one', 'two', 'three']
    print(value_list) # [1, 2, 3]

    # get a list if tuples, each tuple is (key, value)
    key_value_list_of_tuples = [(f, dict1.get(f)) for f in dict1] # each key:val is mapped to a tuple
    print(key_value_list_of_tuples) # [('one', 1), ('two', 2), ('three', 3)]

    ########### dictionary comprehension #################
    # A dictionary comprehension is like a list comprehension, but it constructs a dictionary instead of a list.
    # to return a dict, use braces instead of square brackets, and use colon to separate key:val
    square_dict = {f:dict1.get(f)*dict1.get(f) for f in dict1}
    print(square_dict) # {'one': 1, 'two': 4, 'three': 9}
    filtered_dict = {f:dict1.get(f) for f in dict1 if dict1.get(f) > 1}
    print(filtered_dict) # {'two': 2, 'three': 3}

    # swapping key and value
    swap_dict = {value: key for key, value in dict1.items()}
    print(swap_dict) # {1: 'one', 2: 'two', 3: 'three'}


    ########## set comprehension
    set1 = set(range(5))
    print(set1) # {0, 1, 2, 3, 4}
    set2 = {x*x for x in set1 if x > 2}

    print(set2) # {16, 9} Note: it's unordered, and {} is used for set
    square_set = {x*x for x in range(5)}
    print(square_set) # {0, 1, 4, 9, 16}