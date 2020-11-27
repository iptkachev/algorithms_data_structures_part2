import sys
from typing import List, Tuple
from collections import deque


def emulate_network_packages(packages: List[Tuple[int, int]], buffer_size: int) -> List[int]:
    end_packages_queue = deque(maxlen=buffer_size)
    results = []

    for (arrival, duration) in packages:
        if end_packages_queue and end_packages_queue[0] <= arrival:
            end_packages_queue.popleft()

        if len(end_packages_queue) < buffer_size:
            end_last_package = end_packages_queue[-1] if end_packages_queue else arrival
            end_packages_queue.append(end_last_package + duration)
            results.append(end_last_package)
        else:
            results.append(-1)

    return results


if __name__ == '__main__':
    assert emulate_network_packages([], 3) == []
    assert emulate_network_packages([(0, 1), (0, 2), (0, 4), (0, 0)], 3) == [0, 1, 3, -1]
    assert emulate_network_packages([(0, 0), (0, 0), (0, 0), (0, 0)], 3) == [0, 0, 0, 0]
    assert emulate_network_packages([(0, 5), (0, 6), (0, 4), (0, 5)], 3) == [0, 5, 11, -1]
    assert emulate_network_packages([(0, 1), (0, 2), (0, 4), (0, 0), (1, 1), (1, 0), (2, 0), (2, 1), (3, 1)], 1) == \
        [0, -1, -1, -1, 1, -1, 2, 2, 3]
