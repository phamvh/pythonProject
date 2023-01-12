if __name__ == '__main__':
    """
    sets use braces {}, like dicts. tuples use (). lists use []
    a set can store elements of different types
    duplicates are ignored,
    set can't be accessed by index, just like set in Java
    sets are immutable, like tuples. They cannot be changed after being created
    """

    set1 = {"apple", "banana", 100}
    print(set1)
    print(type(set1)) # <class 'set'>
    print(len(set1))

    # constructor using double parens, not sure why
    set2 = set(("apple", "banana", "peach"))
    print(set2)

    x = set1.pop() # remove and return an arbitrary element
    print(set1) # through this pop() function, looks like set is changeable, no?

    set1.add(x) # add back the popped element, so yeah, seems like set is changeable in python 3.10
    print(set1) # {'apple', 'banana', 100}

    set1.update(set2) # union of set1 and set2, result is stored in set1, duplicates are ignored of course
    print(set1) # {100, 'peach', 'banana', 'apple'}

    set1.remove("peach") # remove "peach". "peach" must be a member, otherwise error raised
    print(set1) # {100, 'apple', 'banana'}

    set1.discard("melon") # remove an element from set if it's a member; if not, do nothing. Better than remove()

    diff = set1.difference(set2) # return the difference of 2 sets: results are in set1, but not in set2
    print(diff) # {100}

    print(set1) # {'banana', 100, 'apple'}
    print(set2) # {'peach', 'banana', 'apple'}
    set1.difference_update(set2) # remove all elements of set1 that are in set2
    print(set1) # {100}
    # added back
    set1.add("banana")
    set1.add("apple")

    x = set1.intersection(set2) # return the intersection of two sets as a new set (elements present in both sets)
    print(x) # {'banana', 'apple'}

    set1.intersection_update(set2) # same as intersection, but the result is stored back in set1 (update set1)
    print(set1) # {'banana', 'apple'}
    set1.add(100) # added back

    print(set1.isdisjoint(set2)) # if intersection is empty. False

    set1.update(set2) # update set1 with the union of itself and set2, meaning add the new ones from set2 to set1
    print(set1) # {'peach', 'banana', 100, 'apple'}
    set1.discard("peach") # remove the newly added

    print(set1.issubset(set2)) # if sets is a subset of set2. False
    print(set1.issuperset(("apple", "banana"))) # if set1 is a superset of another. True

    symDiff = set1.symmetric_difference(set2) # all elements that are in either set1 or set2, but not both
    print(symDiff) # {100, 'peach'}

    set1.symmetric_difference_update(set2) # same as symmetric_difference(), but result is stored in set1
    print(set1)
    # remove new and add back old elements
    set1.discard("peach")
    set1.add("apple")
    set1.add("banana")



