class Person:
    """
    A parent class Person, which has:
     - a class var, similar to static var in Java: personCount
    """
    # similar to static var in Java.
    # to access, use class name, not object: Person.personCount
    personCount = 0

    def __init__(self, name, age):
        self.name = name  # instance var
        self.age = age  # instance var
        Person.personCount += 1  # class var

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def info(self):
        print("name is:", self.name, ", age is ", self.age, ", total persons is", Person.personCount)