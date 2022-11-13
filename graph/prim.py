from __future__ import annotations
from typing import *
from heapq import heappush, heappop
from pydantic.dataclasses import dataclass
from pprint import pprint


@dataclass
class Node:
    is_visited: bool = False
    prev: Optional[int] = None


def do_prim(graph: Dict[int, Dict[int, int]]) -> Dict[int, Node]:
    nodes_info = {key: Node() for key in graph}
    pq = []
    start_node = list(graph)[0]
    nodes_info[start_node].is_visited = True
    for neighbour in graph[start_node]:
        heappush(pq, (graph[start_node][neighbour], start_node, neighbour))
    while pq:
        _, start_node, end_node = heappop(pq)
        if not nodes_info[end_node].is_visited:
            nodes_info[end_node].is_visited = True
            nodes_info[end_node].prev = start_node
            for neighbour in graph[end_node]:
                if not nodes_info[neighbour].is_visited:
                    heappush(pq, (graph[end_node][neighbour], end_node, neighbour))
    return nodes_info


if __name__ == "__main__":
    graph = {
        0: {1: 2, 2: 3, 3: 17, 4: 4},
        1: {0: 2},
        2: {0: 3, 6: 1},
        3: {0: 17, 5: 1},
        4: {0: 4},
        5: {3: 1, 6: 1},
        6: {0: 6, 2: 1, 5: 1}
    }
    pprint(do_prim(graph))
    assert do_prim(graph) == {
        0: Node(is_visited=True, prev=None),
        1: Node(is_visited=True, prev=0),
        2: Node(is_visited=True, prev=0),
        3: Node(is_visited=True, prev=5),
        4: Node(is_visited=True, prev=0),
        5: Node(is_visited=True, prev=6),
        6: Node(is_visited=True, prev=2)
    }
