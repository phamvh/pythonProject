import functools
import operator

if __name__ == '__main__':
    """
   https://www.geeksforgeeks.org/reduce-in-python/
    The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

    Working :  
    
    At first step, first two elements of sequence are picked and the result is obtained.
    
    Next step is to apply the same function to the previously attained result and the number just 
    succeeding the second element and the result is again stored.
    
    This process continues till no more elements are left in the container.
    The final returned result is returned and printed on console.
    """

    lis = [1,2,3,4,5]
    sum = functools.reduce(lambda a,b: a + b, lis)
    print(sum) # 15

    # can use operator which has a bunch of functions already.
    product = functools.reduce(operator.mul, lis)
    print(product) # 120
    print(functools.reduce(operator.add, lis)) # 15



