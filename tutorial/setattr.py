class Person:
    def __init__(self):
        pass
if __name__ == '__main__':
    """
    add a new attr  to an object of an existing class that does not have that attribute
    """
    person = Person()
    print(hasattr(person, "name")) # False
    setattr(person, "name", "Mike")
    print(hasattr(person, "name"))  # True
    print(person.name) # Mike

    # print(getattr(person, name)) # not valid because name is not recognized as a var
    print(getattr(person, "name")) # Mike

    # setattr(person, age, 33) # not valid because age is not recognizable. Need to put it as string
    setattr(person, "age", 33)
    print(person.age) # here it's ok to use age as an attr of an object
    if hasattr(person, "age"): # should check before deleting.
        del person.age
    print(hasattr(person, "age")) # False
    # del person.age this would throw an error as there is no attr age

    def func():
        print("func")
        return # test if this is valid. It is. It is optional to have it. You don't need it like in Java.

    func()
