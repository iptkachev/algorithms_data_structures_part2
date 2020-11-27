from typing import Union, List
import sys


class MaxStack:
    def __init__(self):
        self._max = []

    def push(self, x: int):
        last_max = self._max[-1] if self._max else -1
        self._max.append(max(last_max, x))

    def pop(self):
        self._max.pop()

    def max(self) -> Union[int, None]:
        return self._max[-1] if self._max else 0


if __name__ == '__main__':
    test1 = MaxStack()
    test1.push(5)
    test1.push(0)
    assert test1.max() == 5
    test1.pop()
    assert test1.max() == 5
    test1.pop()
    assert test1.max() == 0

    test2 = MaxStack()
    test2.push(5)
    test2.pop()
    test2.push(3)
    assert test2.max() == 3
    test2.push(9)
    test2.pop()
    test2.push(7)
    assert test2.max() == 7
