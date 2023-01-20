"""
Get all prime numbers from 0 to a given n
"""
import math


def getPrimes(n: int) -> list[int]:
    if n <= 1:
        return []
    flag: list[bool] = [True] * (n + 1)
    flag[0] = False
    flag[1] = False
    sqr = math.floor(math.sqrt(n))
    for i in range(2, n + 1):
        if flag[i]:
            for j in range(i*i, n + 1, i):
                flag[j] = False
    result: list[int] = []
    for i in range(2, n + 1):
        if flag[i]:
            result.append(i)
    return result

if __name__ == '__main__':
    print(getPrimes(30))


