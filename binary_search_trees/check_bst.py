from binary_search_trees.bst_traversals import Node, BST


def is_bst_correct(tree: BST, node_index: int, min_key: int = float('-inf'), max_key: int = float('inf')) -> bool:
    is_correct = True
    if not tree:
        return is_correct

    node = tree[node_index]
    if node.left != -1:
        if min_key < tree[node.left].key < node.key:
            is_correct = is_bst_correct(tree, node.left, min_key, node.key)
        else:
            return False

    if node.right != -1 and is_correct:
        if node.key < tree[node.right].key < max_key:
            is_correct = is_bst_correct(tree, node.right, node.key, max_key)
        else:
            return False

    return is_correct


if __name__ == '__main__':
    tree = [
        Node(4, 1, 2), Node(2, 3, 4), Node(5, -1, -1), Node(1, -1, -1),
        Node(3, -1, -1)
    ]
    assert is_bst_correct(tree, 0) is True

    tree = [
        Node(1, 1, 2), Node(2, -1, -1), Node(3, -1, -1)
    ]
    assert is_bst_correct(tree, 0) is False

    tree = [
        Node(10, -1, -1)
    ]
    assert is_bst_correct(tree, 0) is True

    tree = []
    assert is_bst_correct(tree, 0) is True

    tree = [
        Node(4, 1, 2), Node(2, 3, 4), Node(6, 5, 6),
        Node(1, -1, -1), Node(3, -1, -1), Node(5, -1, -1),
        Node(7, -1, -1)
    ]
    assert is_bst_correct(tree, 0) is True

    tree = [
        Node(4, 1, -1), Node(-2, 2, 3), Node(-3, -1, -1),
        Node(-1, -1, -1)
    ]
    assert is_bst_correct(tree, 0) is True

    tree = [
        Node(15, 1, -1), Node(4, 2, 3), Node(3, -1, -1), Node(7, 4, 5), Node(5, -1, -1), Node(16, -1, -1)
    ]
    assert is_bst_correct(tree, 0) is False
