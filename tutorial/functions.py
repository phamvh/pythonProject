


if __name__ == '__main__':
    """
    Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
    Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside 
    these parentheses.

    The first statement of a function can be an optional statement - the documentation string of the function 
    or docstring.

    The code block within every function starts with a colon (:) and is indented.

    The statement return [expression] exits a function, optionally passing back an expression to the caller. 
    A return statement with no arguments is the same as return None.
    
    
    Syntax:
    
    def function_name(param1, param2):
        "function_docstring"
        function suite
        return [expression]
        
        
    There are four types of arguments in Python functions:
    1. Required arguments (no default value provided)
    2. Named arguments, or keyword arguments when calling: give names when call, such as myFunc(name = "Elon", age = 50)
    3. Default arguments when defining, and they become optional when calling.
         def myFunc(name = "John", age = "20):
    4. variable-length args, like ... in Java, when defining.         
 
    """


    # Required args: all args are required here because no default values are provided.
    def info(name, age):
        print("Name is", name, ", and age is", age)
        return


    # when calling, name is required, but age is optional because it has a default value = 50
    def info_optional_args(name, age=50):
        print("Name is", name, ", and age is", age)
        return

    # use named arguments when calling.
    info(name = "Elon", age= 55)  # Name is Elon , and age is 55

    # age is not passed in because it's optional
    info_optional_args("Elon")  # Name is Elon , and age is 50


    def info_companies(name, *companies):
        """
        :param name: this is a required argument.
        :param companies: this is optional, and it can be many, thus the * sign. Since the values are comma separated,
                        they are treated as a tuple of value.
        :return:
        """
        print(name, "governs the following companies: ", end="")
        for comp in companies:
            print(comp, end=", ")
        print()

    info_companies("Elon", "Tesla", "Twitter", "Space X")


    # lambda
    """
    A lambda form can take any number of args, but returns just one in the form of an expression.
    It cannot contain any command or multiple expression.
    Lmbda functions have their own namespace, and cannot access vars other than those in their param list and 
    in the global namespace.
    """

    # sum here is a function name. Note that no "return" word is needed, just like a short lambda in Java
    sum = lambda x, y, z: x + y + z
    print(sum(1,2,3))



