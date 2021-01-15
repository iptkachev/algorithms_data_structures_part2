from typing import Tuple, Union


class Node:
    def __init__(self, key: int, parent=None, left=None, right=None):
        self.key: int = key
        self.parent: Node = parent
        self.left: Node = left
        self.right: Node = right
        self.size: int = 1
        self.sum: int = key

    def __repr__(self):
        return f"Node({self.key}, {self.sum}, {self.left}, {self.right})"


class AVL:
    AVL_DEPTH_CONDITION_REBALANCE_TREE = 2

    def __init__(self):
        self._root: Node = None

    def search(self, key: int) -> bool:
        if self._root:
            _, child_node = self._search(key)
            if child_node:
                return True
        return False

    def _search(self, key: int) -> Tuple[Union[Node, None], Union[Node, None]]:
        node = self._root
        parent_node = node.parent
        while node:
            if key == node.key:
                break
            elif key > node.key:
                parent_node = node
                node = node.right
            elif key < node.key:
                parent_node = node
                node = node.left

        return parent_node, node

    def add(self, key: int):
        if not self._root:
            self._root = Node(key)
        else:
            parent_node, child_node = self._search(key)

            if not child_node:
                child_node = Node(key, parent_node)
                if parent_node.key < key:
                    parent_node.right = child_node
                else:
                    parent_node.left = child_node

                self._balance_tree(child_node)

    def delete(self, key: int):
        if not self._root:
            return

        _, node = self._search(key)
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

        del node

    def _delete_leaf(self, node: Node):
        # когда лист - это корень
        if not node.parent:
            self._root = None
        else:
            # зануление ссылки из родителя на левый лист, который хотим удалить
            if node.parent.left == node:
                node.parent.left = None
            # зануление ссылки из родителя на правый лист, который хотим удалить
            elif node.parent.right == node:
                node.parent.right = None

            self._balance_tree(node.parent)
            node.parent = None

    def _delete_full_node(self, node: Node):
        new_root = self._max_node(node.left)
        old_parent_new_root = new_root.parent

        if new_root == node.left:
            node.left = None  # чтобы не было циклической ссылки
        else:
            if new_root.left:
                new_root.parent.right = new_root.left
            else:
                new_root.parent.right = None  # чтобы не было циклической ссылки

            new_root.left = node.left
            new_root.left.parent = new_root

        new_root.right = node.right
        new_root.right.parent = new_root

        new_root.parent = node.parent

        if not new_root.parent:
            self._root = new_root
        else:
            # вершина не корень
            # Тут обязательно нужно знать для родителя удаляемая вершина левая или правая,
            # чтобы правильно изменить ссылку из этой вершины на новый корень (который встанет вместо удаленной)
            if new_root.parent.right == node:
                new_root.parent.right = new_root

            elif node.parent.left == node:
                node.parent.left = new_root

        if old_parent_new_root == node:
            self._balance_tree(new_root)
        else:
            self._balance_tree(old_parent_new_root)

    def _delete_half_node(self, node: Node):
        # вершина корень
        if not node.parent:
            if node.right:
                node.right.parent = None
                self._root = node.right
            elif node.left:
                node.left.parent = None
                self._root = node.left
            self._balance_tree(self._root)
        else:
            # вершина не корень
            # Тут обязательно нужно знать для родителя удаляемая вершина левая или правая,
            # чтобы правильно изменить ссылки детей этой вершины для родителя этой же вершины
            if node.parent.right == node:
                node.parent.right = node.right or node.left
                # сделан такой хак (node.parent.right.parent), чтобы отдельно не прописывать if для node.right и node.left
                node.parent.right.parent = node.parent

            elif node.parent.left == node:
                node.parent.left = node.right or node.left
                # аналогично выше
                node.parent.left.parent = node.parent

            self._balance_tree(node.right or node.left)

    def _max_node(self, node: Node) -> Node:
        while node.right:
            node = node.right
        return node

    def find_sum(self, left_key: int, right_key: int, node=-1) -> int:
        sum_value = 0
        if not self._root or left_key > right_key:
            return sum_value

        if node == -1:
            node = self._root

        if left_key <= node.key <= right_key:
            sum_value += node.key
        if node.left and left_key <= node.key:
            sum_value += self.find_sum(left_key, right_key, node.left)
        if node.right and right_key >= node.key:
            sum_value += self.find_sum(left_key, right_key, node.right)
        return sum_value

    def find_sum2(self, left_key: int, right_key: int) -> int:
        sum_value = 0
        if left_key > right_key or not self._root:
            return sum_value

        left_key_sum, _ = self._get_sum_greater_and_or_equal(left_key)
        right_key_sum, is_right_included = self._get_sum_greater_and_or_equal(right_key)
        sum_value = left_key_sum - right_key_sum
        if is_right_included:
            sum_value += right_key

        return sum_value

    def _get_sum_greater_and_or_equal(self, key: int) -> Tuple[int, bool]:
        """

        """
        is_key_exist = False
        node = self._root
        greater_or_equal_sum = node.sum

        while node:
            if key == node.key:
                is_key_exist = True
                if node.left:
                    greater_or_equal_sum -= node.left.sum
                break
            elif key > node.key:
                if node.left:
                    greater_or_equal_sum -= node.left.sum
                greater_or_equal_sum -= node.key
                node = node.right
            elif key < node.key:
                node = node.left

        return greater_or_equal_sum, is_key_exist

    def _balance_tree(self, node: Node):
        """
        By https://ru.wikipedia.org/wiki/АВЛ-дерево
        """
        while node:
            left_size = self._get_depth_size(node.left)
            right_size = self._get_depth_size(node.right)

            if abs(right_size - left_size) >= self.AVL_DEPTH_CONDITION_REBALANCE_TREE:
                if right_size - left_size >= self.AVL_DEPTH_CONDITION_REBALANCE_TREE:
                    # высота правого поддерева у правого ребенка
                    right_right_size = self._get_depth_size(node.right.right)
                    # высота левого поддерева у правого ребенка
                    right_left_size = self._get_depth_size(node.right.left)
                    if right_left_size <= right_right_size:
                        node = self._small_left_rotate(node)
                    else:
                        node = self._big_left_rotate(node)

                elif left_size - right_size >= self.AVL_DEPTH_CONDITION_REBALANCE_TREE:
                    # аналогично
                    left_right_size = self._get_depth_size(node.left.right)
                    left_left_size = self._get_depth_size(node.left.left)
                    if left_right_size <= left_left_size:
                        node = self._small_right_rotate(node)
                    else:
                        node = self._big_right_rotate(node)

                # после балансировки нужно пересчитать высоты и подсуммы
                self._update_depth_size(node.left)
                self._update_depth_size(node.right)
                self._update_sum(node.left)
                self._update_sum(node.right)

            self._update_sum(node)
            self._update_depth_size(node)
            node = node.parent

    def _small_left_rotate(self, root: Node):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        self._update_parent_references(root, new_root)
        self._update_child_reference_from_root_to_new_root(root, new_root)

        return new_root

    def _big_left_rotate(self, root: Node):
        new_root = root.right.left
        new_root_right = new_root.right
        new_root_left = new_root.left

        root.right.left = new_root_right
        new_root.right = root.right
        root.right = new_root_left
        new_root.left = root

        self._update_parent_references(root, new_root)
        self._update_child_reference_from_root_to_new_root(root, new_root)

        return new_root

    def _small_right_rotate(self, root: Node):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        self._update_parent_references(root, new_root)
        self._update_child_reference_from_root_to_new_root(root, new_root)

        return new_root

    def _big_right_rotate(self, root: Node):
        new_root = root.left.right
        new_root_left = new_root.left
        new_root_right = new_root.right

        root.left.right = new_root_left
        new_root.left = root.left
        root.left = new_root_right
        new_root.right = root

        self._update_parent_references(root, new_root)
        self._update_child_reference_from_root_to_new_root(root, new_root)

        return new_root

    def _update_parent_references(self, root: Node, new_root: Node):
        """
        Для малых вращений делаются лишние действия, но это полиморфно для обоих видов вращений.
        """
        new_root.parent = root.parent
        root.parent = new_root
        if new_root.left:
            new_root.left.parent = new_root
        if new_root.right:
            new_root.right.parent = new_root
        if new_root.left.right:
            new_root.left.right.parent = new_root.left
        if new_root.right.left:
            new_root.right.left.parent = new_root.right

    def _update_child_reference_from_root_to_new_root(self, root: Node, new_root: Node):
        if root == self._root:
            self._root = new_root
        else:
            # поменять ссылку из родителя root на new_root
            if new_root.parent.left == root:
                new_root.parent.left = new_root
            elif new_root.parent.right == root:
                new_root.parent.right = new_root

    def _get_depth_size(self, node: Node) -> int:
        return node.size if node else 0

    def _update_depth_size(self, node: Node):
        if node:
            left_size = self._get_depth_size(node.left)
            right_size = self._get_depth_size(node.right)
            node.size = max(left_size, right_size) + 1

    def _get_sum(self, node: Node) -> int:
        return node.sum if node else 0

    def _update_sum(self, node: Node):
        if node:
            left_sum = self._get_sum(node.left)
            right_sum = self._get_sum(node.right)
            node.sum = sum((left_sum, right_sum, node.key))


if __name__ == '__main__':
    tree = AVL()
    tree.search(10)
    tree.add(10)
    tree.add(20)
    tree.add(15)
    tree.add(14)
    tree.add(17)
    tree.add(17)
    assert tree.search(10) == True
    assert tree.search(16) == False
    tree.delete(10)
    assert tree.search(10) == False
    assert tree.find_sum2(8, 9) == 0
    assert tree.find_sum2(9, 14) == 14
    assert tree.find_sum2(14, 14) == 14
    assert tree.find_sum2(14, 15) == 29
    assert tree.find_sum2(14, 17) == 46
    tree.add(7)
    tree.add(6)
    tree.add(5)
    tree.add(4)
    tree.add(3)
    tree.add(2)
    tree.add(1)
    tree.find_sum2(14, 16)
    tree.delete(6)
    tree.delete(7)
    tree.delete(14)
    assert tree.find_sum2(15, 15) == 15
    assert tree.find_sum2(5, 19) == 37
    assert tree.find_sum2(-100, 100) == 67
    tree.delete(5)
    tree.add(100)
    tree.add(10)
    tree.add(200)
    tree.add(9)

