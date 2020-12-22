from __future__ import annotations
from typing import List, Tuple, Union


class Node:
    def __init__(self, key: int, parent: Node = None, left: Node = None, right: Node = None):
        self.key: int = key
        self.parent: Node = parent
        self.left: Node = left
        self.right: Node = right
        self.size: int = None

    def __repr__(self):
        return f"Node({self.key}, {self.left}, {self.right})"


class AVL:
    def __init__(self):
        self._root: Node = None

    def add(self, item: int):
        if not self._root:
            self._root = Node(item)
        else:
            parent_node, child_node = self._search(item)

            if not child_node:
                child_node = Node(item, parent_node)
                if parent_node.key < item:
                    parent_node.right = child_node
                else:
                    parent_node.left = child_node

    def delete(self, item: int):
        _, node = self._search(item)
        if not node:
            return

        # когда удаляемая вершина - лист
        if not node.right and not node.left:
            self._delete_leaf(node)

        # когда у удаляемой вершины есть оба поддерева
        elif node.right and node.left:
            self._delete_full_node(node)

        # когда у удаляемой вершины есть только одно поддерево
        elif node.right or node.left:
            self._delete_half_node(node)

    def _delete_leaf(self, node):
        # когда лист - это корень
        if not node.parent:
            self._root = None
        # зануление ссылки из родителя на левый лист, который хотим удалить
        elif node.parent.left == node:
            node.parent.left = None
        # зануление ссылки из родителя на правый лист, который хотим удалить
        elif node.parent.right == node:
            node.parent.right = None

    def _delete_full_node(self, node):
        max_node_in_left = self._max_node(node.left)
        max_node_in_left.right = node.right
        max_node_in_left.left = node.left
        max_node_in_left.parent.right = None

        if not node.parent:
            max_node_in_left.parent = None
            self._root = max_node_in_left
        # не корень.
        # Тут обязательно нужно знать для родителя удаляемая вершина левая или правая (?),
        # чтобы правильно изменить ссылки детей этой вершины для родителя удаляемой вершины
        elif node.parent.right == node:
            node.parent.right = max_node_in_left
            max_node_in_left.parent = node.parent

        elif node.parent.left == node:
            node.parent.left = max_node_in_left
            max_node_in_left.parent = node.parent

    def _delete_half_node(self, node):
        # вершина корень
        if not node.parent:
            if node.right:
                node.right.parent = None
                self._root = node.right
            elif node.left:
                node.left.parent = None
                self._root = node.left
        # не корень.
        # Тут обязательно нужно знать для родителя удаляемая вершина левая или правая (?),
        # чтобы правильно изменить ссылки детей этой вершины для родителя вершины
        elif node.parent.right == node:
            node.parent.right = node.right or node.left
            # сделан такой хак (node.parent.right.parent), чтобы отдельно не прописывать if для node.right и node.left
            node.parent.right.parent = node.parent

        elif node.parent.left == node:
            node.parent.left = node.right or node.left
            # аналогично выше
            node.parent.left.parent = node.parent

    def find_sum(self, left: int, right_item: int) -> int:
        pass

    def search(self, item: int) -> bool:
        _, child_node = self._search(item)
        if child_node:
            return True
        return False

    def _search(self, item: int) -> Tuple[Union[Node, None], Union[Node, None]]:
        node = self._root
        parent_node = node.parent
        while node:
            if item == node.key:
                break
            elif item > node.key:
                parent_node = node
                node = node.right
            elif item < node.key:
                parent_node = node
                node = node.left

        return parent_node, node

    def _max_node(self, node: Node):
        while node.right:
            node = node.right
        return node


if __name__ == '__main__':
    tree = AVL()
    tree.add(10)
    tree.add(20)
    tree.add(15)
    print(tree.search(10))
    print(tree.search(16))
    print(tree._root)
    tree.delete(10)
    print(tree.search(10))
    print(tree._search(10))
    print(tree._root)




