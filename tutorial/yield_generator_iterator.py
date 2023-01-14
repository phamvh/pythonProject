"""
https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/


1. The yield statement suspends a function's execution and sends a value back to the caller, but it also
retains enough state to enable the function to resume where it left off.

2. When it resumes, it continues execution immediately AFTER the last yield run.

1. and 2. allow its code to produce a series of values OVER times (seriesl of calls), rather than
computing it once and send it back.

You can provide multiple yield statements, or use awhile loop.

3. Any function that has "yield" is a generator.

4. An iterator is any thing that has __iter__() method, which returns an object that, in turn, has __next__() function.


"""

def simpleGeneratorFunc():
    yield 1
    yield 2
    yield 3 # if try to call more than 3 times, an error will occur

def nextSquare():
    i = 1
    while True: # this yield never finishes
        yield i*i # each time next() is called, it will return i*i, and suspends till the time next() is called again.
        i += 1

class SimpeIteator:
    """
    https://www.geeksforgeeks.org/iterators-in-python/

    An iterator is anything that has __iter__() method, which returns an object that, in turn, has __next__() function.
    In other words, the __iter__() function basically returns a generator - the same thing that a generator function returns.

    The main idea of Iterator is that a generator can be encapsulated in an object, instead of calling a generator function.
    So basically, inside the __iter__ function, you can just call another generator function and returns its returned value.
    """
    def __init__(self):
        pass

    def __iter__(self):
        """
        Here, just need to return something that has __next__() function. In other words, it needs to return the
        same thing as a generator function returns. So here, we just call simpleGeneratorFunc().
        An object that has the __next__() function is called an Iterator object.
        So a generator function returns an iterator object.
        """
        return simpleGeneratorFunc()

class SquareIterator:
    """
    Here, a class itself has the __next__() function.
    """
    def __init__(self, limit: int):
        self.limit = limit

    def __iter__(self):
        self.i = 1
        ## here, class ComplexIterator has __next__() function, so we can return "self"
        return self

    def __next__(self):
        """
        Note: we don't need to use "yield" here. Yield is used to return a generator (something that has __next__() func.
        Here, we are inside the __next__() function already. So for an iterator class, we don't need to use yield
        """
        val = self.i * self.i
        if val > self.limit:
            raise StopIteration

        self.i += 1
        return val

if __name__ == '__main__':
    for num in simpleGeneratorFunc():
        print(num, end=", ") # 1, 2, 3,

    print()
    # this returns a generator object, which needs some loop to go through. Or you need to call next() function
    print(simpleGeneratorFunc()) # <generator object simpleGeneratorFunc at 0x100261a10>

    gen = simpleGeneratorFunc()
    print(gen.__next__()) # 1
    print(gen.__next__()) # 2
    print(gen.__next__()) # 3
    # print(gen.__next__()) # caused an error, as there are only 3 yields.

    gen1 = nextSquare()
    # use next() function instead of a loop. next() actually calls __next__() of the generator (polymorphism via function)
    print(next(gen1)) # 1
    print(next(gen1)) # 4

    print()
    simple_iterator = SimpeIteator()
    for i in simple_iterator:
        print(i, end=", ") # 1, 2, 3,

    print()
    square_iterator = SquareIterator(25) # set limit to 5
    for i in square_iterator:
        print(i, end=", ") # 1, 4, 9, 16, 25,