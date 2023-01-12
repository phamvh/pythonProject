if __name__ == '__main__':
    """
    Use assert to raise an error
    """

    # assert 1 == 2 # raise AssertionError

    def kelvin_to_fahrenheit(temp):
        # raise an error if temp < 0
        assert (temp >= 0), "invalid value as kelvin needs to be on-negative"
        return (temp - 273)*1.8 + 32

    print(kelvin_to_fahrenheit(20))
    # print(kelvin_to_fahrenheit(-10))  # --> AssertionError: invalid value as kelvin needs to be on-negative


    """
    Use try ... except ... else to catch exceptions.
    else gets executed when no exception is thrown within the try block
    """
    try:
        f = open("test.file", "w")
        f.write("Hello file")
    except (IOError, NameError, TypeError) as err: # or if one type, then without parens: except IOError:
        print("some error occurred")
        print(err)
    else:
        print("wrote something to file")
        f.close()


    # To catch all exception, don't specify any type of exception after the word "except"
    try:
        f = open("test.file", "r")  # open for read-only
        f.write("Hello file")       # then try to write
    except:    # no specific type of exception here, so it will catch all types of exceptions
        print("some IOError occurred")
    else:
        print("wrote something to file")
    finally:
        print("this executes no matter exceptions occur or not, like in Java")
        f.close()


    # Get the argument of an exception. Use as to assign an exception to a var to be used later.
    try:
        f = open("test.file", "r")  # open for read-only
        f.write("Hello file")       # then try to write
    except IOError as err:  # here, IOError is assigned to err, which is later printed out.
        print("some IOError occurred:")
        print(err)
    finally:
        f.close()


    # Raise an exception
    try:
        raise ValueError("Some invalid value")
    except ValueError as e:
        print(e)  # Some invalid value
