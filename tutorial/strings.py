if __name__ == '__main__':
    """
    Strings can be created using single, double or tripple quotes
    Python does NOT support character type. A char is treated as a string of length 1
    """
    s = "0123456789"
    s = '0123456789'
    s = '''0123456789'''
    print(s)
    print(s[0]) # print first char, similar to charAt(i) in java
    print(s[2:5]) # substring, from 3rd to 5th, including 3d, excluding 5th, just like java
    print(s[2:])  # substring, from 3rd till the end.
    print(s * 2)  # print str twice -- so weird
    s = s * 2   # this is also a valid operation: concatenate a string to itself.
    print(s)
    s = "0123456789"
    s = s + " Hello 123"  # concatenate two strings
    print(s)
    print(len(s)) # length, need to call function len, no built-in function from string itself.
    print(s.lower())
    print(s.upper())
    print(s.startswith("123")) # false
    print(s.startswith("0123")) # true
    print(s.find("123")) # 1 - return the lowest index (first occurrence)
    print(s.rfind("123")) # return the highest index (last occurrence)
    print(s.count("123")) # count the number of occurrences
    print(s.isdigit())
    print(s.isnumeric())
    print(s.split(" ")) # return a list of subs seperated by a space char

    s = "0123456789"
    print("0" in s)  # True
    print("234" in s)  # True as substring
    print("321" in s)  # False
    print("321" not in s)  # True

    # raw string. use r or R right before the first qupote of a string to indicate a raw string
    # in a raw string, all special chars, like \n, are escapted and treated as strings
    print(r"hello \n you")  # hello \n you

    #formatting string
    # the percent sign is needed to separate the formatting string and the arguments
    print("My name is %s and weight is %d kg!" % ('Zara', 21))

    # Use format method. use named placeholders for better clarity
    s = "My name is {name}, and my age is {age}".format(name = "Andy", age = 10)
    print(s)
    # or without names like this
    s = "My name is {}, and my age is {}".format("Mike", 33)
    print(s)
    # or use numbers
    s = "My name is {0}, and my age is {1}".format("Mike", 33)
