from tutorial.classes.Person import Person


class Student(Person):
    """
     A child class that extends Person
    """
    studentCount = 0  # class var

    def __init__(self, name, age, school):
        super().__init__(name, age)  # call super constructor
        #self.name = name
        #self.age = age
        self.school = school
        Student.studentCount += 1

    def get_school(self):
        return self.school

    def info(self):  # override parent method
        print("name is:", self.name, ", age is ", self.age, ", school is ", self.school, ", total students is", Student.studentCount)
