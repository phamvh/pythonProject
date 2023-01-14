"""
In python, polymorphism can be achieved through classes like in Java.
In addition, it can also be achieved through functions.
Example: len() function can take any object: list, tuple, string, etc.
The truth is, the len() function calls the len() function of its input object:

def len(obj):
    return obj.len()

So it delegates the call to the function of the input object, and that's how it can work on so many objects.
Similar to method sorted(), which delegates calls to its input object sort()
"""

lis = [1,2,3]
dic = {1:1, 2:2}
s = "hello"

len(lis)
len(dic)
len(s)

# we know that list, dict and string all have their len() functions:

# Similarly, the builtin sorted method
sorted(lis)
lis.sort()

sorted(s)
# actually string doesn't seem to have sort method, maybe by other name, or maybe I am wrong this this example

