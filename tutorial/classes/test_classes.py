from tutorial.classes.Person import Person
from tutorial.classes.Student import Student

if __name__ == '__main__':
    p = Person("John", 20)
    print(p.name, p.age)
    p.info()

    s = Student("Elon", 50, "USC")
    s.info()
    p.info()


    print(isinstance(s, Student))  # True
    print(isinstance(s, Person))   # True cuz it is a subclass
    print(isinstance(p, Student))   # False
    print(issubclass(Student, Person))  # True
    print(issubclass(Person, Student))  # False