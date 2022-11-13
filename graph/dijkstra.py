from __future__ import annotations
from typing import *
from heapq import heappush, heappop
from pydantic.dataclasses import dataclass
from pprint import pprint


@dataclass
class Node:
    prev: Optional[int] = None
    is_visited: bool = False
    dist: Union[float, int] = float("inf")


def do_dijkstra(graph: Dict[int, Dict[int, int]], start: int) -> Dict[int, Node]:
    nodes_info = {node: Node() for node in graph}
    pq = [(start, 0)]
    while pq:
        weight, node_id = heappop(pq)
        if not nodes_info[node_id].is_visited:
            nodes_info[node_id].is_visited = True
            for neighbour_id in graph.get(node_id, []):
                new_dist = weight + graph[node_id][neighbour_id]
                if new_dist < nodes_info[neighbour_id].dist and not nodes_info[neighbour_id].is_visited:
                    nodes_info[neighbour_id] = Node(dist=new_dist, prev=node_id)
                    heappush(pq, (new_dist, neighbour_id))

    return nodes_info


if __name__ == "__main__":
    graph = {
        0: {1: 2, 2: 5, 3: 4},
        1: {2: 1, 3: 2},
        2: {0: 5, 3: 0},
        3: {}
    }
    pprint(do_dijkstra(graph, 0))
    assert do_dijkstra(graph, 0) == {
        0: Node(prev=None, is_visited=True, dist=float("inf")),
        1: Node(prev=0, is_visited=True, dist=2.0),
        2: Node(prev=1, is_visited=True, dist=3.0),
        3: Node(prev=2, is_visited=True, dist=3.0)
    }
