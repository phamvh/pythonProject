
from math import fabs, floor, ceil, exp, e, pi, sqrt
from random import choice, randrange, random, seed, shuffle, uniform

if __name__ == '__main__':
    print(abs(-1.2))
    print(fabs(-1))  # for float, looks the same as abs

    print(floor(1.2))  # 1
    print(ceil(1.2))   # 2

    print(exp(2)) # e^2
    print(e)
    print(pi)

    print(max(1,2,3,4,5,6,7,8,9))  # 9
    print(min(1,2,3,4))            # 1

    print(pow(2,3)) # 8
    print(round(1.2345, 2))  # 1.23  round a number to a given number of decimal digits

    print(sqrt(4))

    # RANDOM ##################
    list1 = [1,2,3,4,5]
    print(choice(list1))  # returna random item from a non-empty sequence, such as list, tuple or string

    print(randrange(1,10,1))  # Choose a random item from range(start, stop[, step]).

    print(random())  # a random float r: 0 <= r < 1

    # to generate a random number, one need to provide a seed to start with, which is used to generate randoms.
    seed(10)  # need to call this first before calling random().
    print(random())
    #if same seed is used, same random will be generated
    seed(10) # set seed again to the same old seed
    print(random()) # this should produce the same random number as the previous one due to same seed

    print(uniform(1,2)) # generate a random number in [1,2)

    shuffle(list1) # shuffle a list randomly
    print(list1)

