from typing import Optional
from binarytree import build, Node


def is_bst(tree: Optional[Node], min_val, max_val):

    if tree is None:
        return True

    if tree.val < min_val or max_val < tree.val:
        return False

    return is_bst(tree.left, min_val, tree.val-1) and is_bst(tree.right, tree.val+1, max_val)


if __name__ == '__main__':

    list_of_nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_tree = build(list_of_nodes)

    my_tree.pprint()
    print(is_bst(my_tree, -10000, +10000))





