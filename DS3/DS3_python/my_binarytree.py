from typing import Optional
from binarytree import build, Node


def is_bst(tree: Optional[Node], min_val, max_val):

    if tree is None:
        return True

    if tree.val < min_val or max_val < tree.val:
        return False

    return is_bst(tree.left, min_val, tree.val-1) and is_bst(tree.right, tree.val+1, max_val)


if __name__ == '__main__':

    list_of_nodes = [10, 5, 12, 3, 7, 11, 13, 2, 4, 6]
    my_tree = build(list_of_nodes)

    my_tree.pprint()
    print('is bst == ' + str(is_bst(my_tree, -10000, +10000)))





