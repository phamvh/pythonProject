if __name__ == '__main__':
    """
    list can store elements of different types, which is different from arrays
    lists use square brackets [] like arrays , sets use {}, tuples use (), dicts use {}
    """
    list1 = [1,2,3,"four"]
    list2 = ["five", 6]
    print(type(list1)) # <class 'list'>
    print(list1)
    print(list1 + list2) # concatenate two lists
    print(len(list1))
    print(list1[0]) # like accessing elements in an array
    print(list1[1:3]) # sublist, from 1st to 3rd, including 1st, excluding 3rd
    print(list1[1:]) # sublist from 1st till the end
    list3 = list1 * 2 # similar to string, concatenate a list to itself.
    print(list3)
    print(list3.count("four")) # count the number of occurrences of a value
    list1.reverse() # reverse a list in-place, returns nothing
    print(list1)
    list1.reverse() # just reverse back
    print(list1.pop(3)) # get and remove an element at the given index
    print(list1)
    list1.append("four") # just append back the removed element
    print(list1)
    list1.remove("four") # remove the first occurrence of a value
    list1.append("four") # append it back
    print(list1.index("four")) # return the index of the first occurrence of a value
    print(not list1) # don't know what this does.
    list1[0] = "one" # update the first element of the list
    print(list1)
    list1.append(list2) # add the whole list2 as the LAST ELEMENT of list1 (nested list).
    print(list1) # ['one', 2, 3, 'four', ['five', 6]]
    list1.remove(list2) # just remove the newly added
    list1.extend(list2) # this one is like addAll in java collection,
    print(list1) # ['one', 2, 3, 'four', 'five', 6]
    list1.remove("five")
    list1.remove(6)
    list1.insert(0, "five") # insert an object at the given index
    print(list1) # ['five', 'one', 2, 3, 'four']
    list1.remove("five")
    list1.clear() # clear all contents
    print(list1) # [] empty list now

    # sorting
    list4 = [(4, "four"), (2, "two"), (5, "five"), (3, "three")]  # a list of tuples we want to sort

    def get_key(t):
        return t[0]
    list4.sort(key=get_key)  # pass the get_key function to function sort.
    print(list4)  # [(2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
    list4.sort(key=get_key, reverse=True)
    print(list4)  # [(5, 'five'), (4, 'four'), (3, 'three'), (2, 'two')]
    list4.sort()  # not sure what it uses as key to sort here, but avoid this if the list type is not obvious to compare
    print(list4)

    list1 = [1,2,3,4]
    # list comprehension is like "Stream.map" in Java. It applies a function to every element of a list
    # and return a new list (NOT modifying the existing list)
    list2 = [elem*2 for elem in list1]
    print(list2)  # [2, 4, 6, 8]

