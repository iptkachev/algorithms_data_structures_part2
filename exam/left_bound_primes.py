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


def get_left_prime_bound(diff_between_numbers, count_primes, upper_bound=10**5):
    prime_numbers = []
    range_slice = [1, diff_between_numbers]
    for i in range(range_slice[0], range_slice[1] + 1):
        if is_prime(i):
            prime_numbers.append(i)
    while len(prime_numbers) != count_primes and range_slice[1] <= upper_bound:
        range_slice[0] += 1
        range_slice[1] += 1
        if prime_numbers[0] < range_slice[0]:
            prime_numbers.pop(0)
        if is_prime(range_slice[1]):
            prime_numbers.append(range_slice[1])
    if range_slice[1] > upper_bound:
        return -1
    return range_slice[0]


if __name__ == '__main__':
    # assert 2 == get_left_prime_bound(2, 2)
    # assert 1 == get_left_prime_bound(3, 2)
    assert 20 ==get_left_prime_bound(6, 1)

    # queries = int(input())
    # for _ in range(queries):
    #     diff_between_numbers, count_primes = map(int, input().split())
    #     print(get_left_prime_bound(diff_between_numbers, count_primes))
