from typing import List, Set, Tuple, ClassVar, Any

if __name__ == '__main__':
    """
    Cheat sheet for Python 3 typing
    https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html 
    """

    ###### Variables
    age: int = 1
    a: int
    child: bool

    x: int = 1
    x: float = 1.0
    x: bool = True
    x: str = "test"
    x: bytes = b"test"

    ##### Useful built-in types
    # For collections on Python 3.9+, the type of the collection item is in brackets
    x: list[int] = [1]
    x: set[int] = {6, 7}
    # Or you can use the redefined names that start with a capital letter
    x: List[int]
    x: Set[int]

    # For mappings, we need the types of both keys and values
    x: dict[str, float] = {"field": 2.0}  # Python 3.9+

    # For tuples of fixed size, we specify the types of all the elements
    x: tuple[int, str, float] = {1, "hello", 1.2} # Python 3.9+
    # For tuples of variable size, we use one type and ellipsis
    x: tuple[int, ...] = {1,2,3}
    # these won't throw errors
    x: tuple[int] = {1, "hello"} # mixed types
    x: Tuple[int, ...] = {1, "hello"} # No difference between tuple and Tuple, it seems.
    print(x)

    # On Python 3.8 and earlier, the name of the collection type is
    # capitalized, and the type is imported from the 'typing' module
    from typing import List, Set, Dict, Tuple
    x: List[int] = [1]
    x: Set[int] = {6, 7}
    x: Dict[str, float] = {"field": 2.0}
    x: Tuple[int, str, float] = (3, "yes", 7.5)
    x: Tuple[int, ...] = (1, 2, 3)

    from typing import Union, Optional

    # On Python 3.10+, use the | operator when something could be one of a few types
    x: list[int | str] = [3, 5, "test", "fun"]  # Python 3.10+
    # On earlier versions, use Union
    x: list[Union[int, str]] = [3, 5, "test", "fun"]

    # Use Optional[X] for a value that could be None
    # Optional[X] is the same as X | None or Union[X, None]
    x: Optional[str] = "something" if True else None
    print(x) # something, no wrapper. Just use it as String
    print(type(x)) # <class 'str'>
    if x is not None:
        print(x.upper())
    # or use assert if it HAS to be not None
    assert x is not None
    print(x.lower())


    ### Read more about typed functions here: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
    #### FUNCTIONS
    def stringify(num: str) -> str:
        return str(num)

    # multiple args
    def sum(num1: int, num2: int) -> int:
        return num1 + num2

    # If a function does not return a value, use None as the return type
    # Default value for an argument goes after the type annotation
    def show(name: str, age: int = 20) -> None:
        print(name, age)

    # A generator function that yields ints is secretly just a function that
    # returns an iterator of ints, so that's how we annotate it
    from typing import Iterator, Union, Optional

    def gen(n: int) -> Iterator[int]:
        i = 0
        while i < n:
            yield i
            i += 1

    for i in gen(4):
        print(i, end=", ") # 0, 1, 2, 3,
    print()

    # Mypy understands positional-only and keyword-only arguments
    # Positional-only arguments can also be marked by using a name starting with
    # two underscores
    def quux(x: int, /, *, y: int) -> None:
        """
        anything before / must be positional args
        anything after * must be keyword args
        """
        pass

    quux(3, y=5)  # Ok
    #quux(3, 5)  # error: Too many positional arguments for "quux"
    #quux(x=3, y=5)  # error: Unexpected keyword argument "x" for "quux"

    #from typing import reveal_type

    # This says each positional arg and each keyword arg is a "str"
    def call(*args: str, **kwargs: str) -> str:
        pass



    #### CLASSES
    class MyClass:
        # You can optionally declare INSTANCE variables in the class body. THis is NOT static
        attr: int
        # This is an instance variable with a default value
        charge_percent: int = 100
        # The "__init__" method doesn't return anything, so it gets return
        # type "None" just like any other method that doesn't return anything
        def __int__(self) -> None:
            pass

        # For instance methods, omit type for "self"
        def func1(self, num: int, s: str) -> str:
            self.attr = 1  ##
            pass

    # User-defined classes are valid as types in annotations
    x: MyClass = MyClass

    # You can also declare the type of an attribute in "__init__"
    class Box:
        def __int__(self) -> None:
            self.items: list[int] = []

    # You can use the ClassVar annotation to declare a class variable
    class Car:
        name: str   # this is a INSTANCE variable
        seats: ClassVar[int] = 4  # this is a CLASS var of type int. ClassVar is like a way for generics.
        passengers: ClassVar[list[str]]  # another class var

        def __int__(self) -> None:
            self.name = "Elon"  # see!! instance var
            Car.seats = 5       # see!! class var

    # If you want dynamic attributes on your class, then
    # override "__setattr__" or "__getattr__":
    # - "__getattr__" allows for dynamic access to names
    # - "__setattr__" allows for dynamic assignment to names
    class A:
        # This will allow assignment to any A.x, if x is the same type as "value"
        # (use "value: Any" to allow arbitrary types)
        def __setattr__(self, key: str, value: int) -> None:
            pass

        def __setattr__(self, key: int, value: Any) -> None:
            pass

        # This will allow access to any A.x, if x is compatible with the return type
        def __getattr__(self, name: str) -> int:
            pass










