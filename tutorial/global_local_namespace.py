if __name__ == '__main__':
    """
    Variables are names (identifiers) that map to objects. 
    A namespace is a dictionary of variable names (keys) and their corresponding objects (values).
    
    A Python statement can access variables in a local namespace and in the global namespace. 
    If a local and a global variable have the same name, the local variable shadows the global variable.
    
    Each function has its own local namespace. Class methods follow the same scoping rule as ordinary functions.

    Python makes educated guesses on whether variables are local or global. 
    It assumes that any variable assigned a value in a function is local.

    Therefore, in order to assign a value to a global variable within a function, you must first use the global statement.
    Example inside a function:
    
    global total
    total = total * 2
    
    Without line 17, line 18 would throw an error, because we are trying to access total (the right side of expression),
    which is assumed by python to be a local var, even though total was already declared outside the method.
    See details here: https://www.tutorialspoint.com/python/python_modules.htm

    The statement global VarName tells Python that VarName is a global variable. 
    Python stops searching the local namespace for the variable.
    """