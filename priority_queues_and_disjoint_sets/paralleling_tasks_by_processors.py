import sys
from typing import List
from dataclasses import dataclass


@dataclass
class Node:
    accumulated_time: int
    n_processor: int


class MinHeap:
    def __init__(self, array: List[Node]):
        self.array = array

    def sift_down(self, i: int):
        min_index = i
        left_index = 2 * i + 1 if len(self.array) > 2 * i + 1 else None
        right_index = 2 * i + 2 if len(self.array) > 2 * i + 2 else None

        is_less_time_or_equal_time_and_less_processor = lambda side_index: (
            self.array[side_index].accumulated_time < self.array[min_index].accumulated_time or
            (
                self.array[side_index].accumulated_time <= self.array[min_index].accumulated_time and
                self.array[side_index].n_processor < self.array[min_index].n_processor
            )
        )

        if left_index and is_less_time_or_equal_time_and_less_processor(left_index):
            min_index = left_index

        if right_index and is_less_time_or_equal_time_and_less_processor(right_index):
            min_index = right_index

        if min_index != i:
            self._swap(i, min_index)
            self.sift_down(min_index)

    def _swap(self, a_index: int, b_index: int):
        a_node = self.array[a_index]
        self.array[a_index] = self.array[b_index]
        self.array[b_index] = a_node


if __name__ == '__main__':
    n_processors, n_tasks = list(map(int, sys.stdin.readline().rstrip().split()))
    tasks = list(map(int, sys.stdin.readline().rstrip().split()))

    heap_processors = MinHeap([Node(0, i) for i in range(n_processors)])
    for task_time in tasks:
        nearest_free_processor = heap_processors.array[0]
        print(nearest_free_processor.n_processor, nearest_free_processor.accumulated_time)
        nearest_free_processor.accumulated_time += task_time
        heap_processors.sift_down(0)
