from tutorial.classes.Person import Person


class Student(Person):
    """
     A child class that extends Person
    """
    studentCount = 0  # class var

    def __init__(self, name, age, school):
        # To call the constructor of the parent class, use the parent class name.
        Person.__init__(self, name, age)
        # or you can use super() to call __init__().
        # Since super() already returns an obj, you don't need to pass "self" to it like above.
        # But if you have multi parents, you need to use the method above as super() becomes ambiguous.
        super().__init__(name, age) # this call is redudant though, as we already did in line 12.


        self.school = school
        Student.studentCount += 1

    def get_school(self):
        return self.school

    def info(self):  # override parent method
        print("name is:", self.name, ", age is ", self.age, ", school is ", self.school, ", total students is", Student.studentCount)
