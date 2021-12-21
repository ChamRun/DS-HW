from binarytree import Node


def t(tree):
    if tree is None:
        return 0

    return (1 + max(t(tree.left), t(tree.right)))


if __name__ == '__main__':
    tree = Node(10)
    tree.left = Node(10)
    tree.left.left = Node(10)
    tree.left.right = Node(10)
    tree.left.right.left = Node(10)
    tree.left.right.right = Node(10)

    tree.right = Node(10)
    tree.right.left = Node(10)
    tree.right.right = Node(10)

    tree.pprint()
    print(t(tree))