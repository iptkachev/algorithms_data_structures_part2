from typing import List


def find_tree_height(tree_by_parents: List[int]) -> int:
    adjacency_lists = [[] for _ in range(len(tree_by_parents))]
    for i, node_parent in enumerate(tree_by_parents):
        if node_parent > -1:
            adjacency_lists[node_parent].append(i)
        else:
            root_node_index = i
    return depth_width_search(adjacency_lists, root_node_index)


def depth_width_search(adjacency_lists: List[List[int]], root_node_index: int) -> int:
    queue_layers = [[root_node_index]]
    height = 1
    while queue_layers:
        nodes_layer = queue_layers.pop(0)
        if is_nodes_have_descendent(adjacency_lists, nodes_layer):
            height += 1
            layer = []
            for children in nodes_layer:
                layer.extend(adjacency_lists[children])
            queue_layers.append(layer)

    return height


def is_nodes_have_descendent(adjacency_lists: List[List[int]], nodes_layer: List[int]) -> bool:
    for node in nodes_layer:
        if adjacency_lists[node]:
            return True
    return False


if __name__ == '__main__':
    assert find_tree_height([4, -1, 4, 1, 1]) == 3
    assert find_tree_height([-1, 0, 4, 0, 3]) == 4
    assert find_tree_height([9, 7, 5, 5, 2, 9, 9, 9, 2, - 1]) == 4
