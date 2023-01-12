if __name__ == '__main__':
    """
    Use match for switching in Python.
    You can match a single value or a tuple
    """
    x = 5
    match x:
        case 1:
            print("one") # No need of break like in Java
        case 5:
            print("five")
        case 10:
            print("ten")
        case 11 | 12: # this or that, super comvenient
            print("eleven or twelve")
        case _:
            print("default")

    a, b = 1, 2
    match (a,b): # you can even match a tuple
        case (1,1):
            print("one one")
        case (1,2):
            print("one two")
        case _:
            print("default")

    match [1,2]: # or match a list, or even a dict
        case [1,1]:
            print("one one")
        case [2,2]:
            print("two two")
        case [1,2]:
            print("one two")
        case _:
            print("default")

