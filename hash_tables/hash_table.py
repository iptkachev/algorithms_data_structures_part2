from __future__ import annotations
from typing import Union


def polynomial_hash(string: str, m: int, x: int = 263, p: int = 1_000_000_007) -> int:
    """
    для stepik в этом задании только конечная сумма берется по mod p, т.е. sum_polynoms % p % m, а не каждый член.
    :param string:
    :param m: размер hash-таблицы
    :param x: база
    :param p: простое число. Используются, чтобы не допустить переполнения
    :return:
    """
    sum_polynoms = sum(ord(ch) * pow(x, i, p) for i, ch in enumerate(string))
    return sum_polynoms % m


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next: Union[Node, None] = next


class LinkedList:
    """
    pointer
    """
    def __init__(self):
        self.next: Union[Node, None] = None

    def prepend(self, x):
        if self.__getitem__(x) == 'no':
            self.next = Node(x, self.next)

    def __repr__(self):
        repr = ""
        next = self.next
        while next:
            if next.item:
                repr += f" {next.item}"
            next = next.next
        return repr.lstrip()

    def __getitem__(self, item):
        next = self.next
        while next:
            if next.item == item:
                return 'yes'
            next = next.next
        return 'no'

    def __delitem__(self, item):
        next = self.next
        while next:
            if next.item == item:
                next.item = None
                break
            next = next.next


class HashTable:
    def __init__(self, m: int):
        self.size = m
        self.hash_table = [LinkedList() for _ in range(m)]

    def add(self, string: str):
        hash = polynomial_hash(string, self.size)
        self.hash_table[hash].prepend(string)

    def find(self, string: str) -> str:
        hash = polynomial_hash(string, self.size)
        return self.hash_table[hash][string]

    def check(self, i: int) -> LinkedList:
        return self.hash_table[i]

    def delete(self, string: str):
        hash = polynomial_hash(string, self.size)
        del self.hash_table[hash][string]


if __name__ == '__main__':
    m = 5
    hash_table = [LinkedList() for _ in range(m)]

    hash_world = polynomial_hash('world', 5)
    hash_hell0 = polynomial_hash('Hell0', 5)

    hash_table[hash_world].prepend('world')
    hash_table[hash_hell0].prepend('Hell0')

    assert str(hash_table[hash_hell0]) == 'Hell0 world'
    assert str(hash_table[hash_world]) == 'Hell0 world'

    del hash_table[hash_hell0]['Hell0']
    del hash_table[hash_hell0]['sdfsdfs']  # no error
    assert str(hash_table[hash_world]) == 'world'
    
    assert hash_table[hash_world]['world'] == 'yes'
    assert hash_table[hash_world]['Hell0'] == 'no'

    hash_table = HashTable(4)
    hash_table.add('test')
    hash_table.add('test')
