from typing import List


class MinHeap:
    def __init__(self, array: List[int]):
        self.array = array
        self._history_swaps = []

    def build(self):
        for i in range((len(self.array) - 1) // 2, -1, -1):
            self.sift_down(i)

    def sift_down(self, i: int):
        min_index = i
        left_index = 2 * i + 1 if len(self.array) > 2 * i + 1 else None
        right_index = 2 * i + 2 if len(self.array) > 2 * i + 2 else None

        if left_index and self.array[left_index] < self.array[min_index]:
            min_index = left_index

        if right_index and self.array[right_index] < self.array[min_index]:
            min_index = right_index

        if min_index != i:
            self._history_swaps.append((i, min_index))
            self._swap(i, min_index)
            self.sift_down(min_index)

    def _swap(self, a_index: int, b_index: int):
        a_value = self.array[a_index]
        self.array[a_index] = self.array[b_index]
        self.array[b_index] = a_value


if __name__ == '__main__':
    array = [5, 4, 3, 2, 1]
    min_heap = MinHeap(array)
    min_heap.build()
    assert len(min_heap._history_swaps) == 3
    assert min_heap._history_swaps == [(1, 4), (0, 1), (1, 3)]