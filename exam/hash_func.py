from functools import lru_cache
import sys
sys.setrecursionlimit(5000)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


@lru_cache(maxsize=None)
def hash(num):
    if is_prime(num):
        return 1
    min_value = float('inf')
    for i in range(2, num - 1):
        a = num - i
        b = i
        min_value = min(hash(a) + hash(b), min_value)
    return min_value


if __name__ == '__main__':
    print(hash(int(input())))

