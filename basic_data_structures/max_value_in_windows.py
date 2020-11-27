from typing import List
from collections import deque


def get_min_value_per_window(array: List[int], size_window: int) -> List[int]:
    queue = deque()
    maxs = []
    for i in range(size_window):
        while queue and array[i] >= array[queue[0]]:
            queue.popleft()
        queue.appendleft(i)
    maxs.append(array[queue[-1]])

    for i in range(size_window, len(array)):
        while queue and queue[-1] <= i - size_window:
            queue.pop()
        while queue and array[i] >= array[queue[0]]:
            queue.popleft()
        queue.appendleft(i)
        maxs.append(array[queue[-1]])

    return maxs


if __name__ == '__main__':
    assert get_min_value_per_window([1, 42, 6, 2, 7, 3, 9], 1) == [1, 42, 6, 2, 7, 3, 9]
    assert get_min_value_per_window([1, 42, 6, 2, 7, 3, 9], 3) == [42, 42, 7, 7, 9]
    assert get_min_value_per_window([1, 42, 6, 2, 7, 3, 9], 2) == [42, 42, 6, 7, 7, 9]
    assert get_min_value_per_window(range(0, 10), 3) == [2, 3, 4, 5, 6, 7, 8, 9]
    assert get_min_value_per_window(range(10, 0, -1), 3) == [10, 9, 8, 7, 6, 5, 4, 3]
