import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())

phone_book = defaultdict(str)
for _ in range(n):
    query = sys.stdin.readline().rstrip().split()

    if query[0] == 'add':
        phone_book[query[1]] = query[2]
    elif query[0] == 'find':
        print(phone_book.get(query[1], 'not found'))
    elif query[0] == 'del':
        phone_book.pop(query[1], None)