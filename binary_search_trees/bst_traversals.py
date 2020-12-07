from typing import List


class Node:
    def __init__(self, key: int, left: int, right: int):
        self.key = key
        self.left = left
        self.right = right


BST = List[Node]


def traversal(tree: BST, node_index: int, mode: str):
    node = tree[node_index]
    if mode == 'pre_order':
        print(node.key, end=" ")
    if node.left != -1:
        traversal(tree, node.left, mode)
    if mode == 'in_order':
        print(node.key, end=" ")
    if node.right != -1:
        traversal(tree, node.right, mode)
    if mode == 'post_order':
        print(node.key, end=" ")


if __name__ == '__main__':
    tree = [
        Node(4, 1, 2), Node(2, 3, 4), Node(5, -1, -1), Node(1, -1, -1),
        Node(3, -1, -1)
    ]

    traversal(tree, 0, 'in_order')  # 1 2 3 4 5
    print()
    traversal(tree, 0, 'pre_order')  # 4 2 1 3 5
    print()
    traversal(tree, 0, 'post_order')  # 1 3 2 5 4
