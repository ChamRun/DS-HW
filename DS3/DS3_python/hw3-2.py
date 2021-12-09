INT_MIN = -2 ** 32


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Utility function to find maximum sum between any
# two leaves. This function calculates two values:
# 1) Maximum path sum between two leaves which are stored
# in res
# 2) The maximum root to leaf path sum which is returned
# If one side of root is empty, then it returns INT_MIN


def maxPathSumUtil(root, res):
    # Base Case
    if root is None:
        return 0

    # Find maximumsum in left and right subtree. Also
    # find maximum root to leaf sums in left and right
    # subtrees ans store them in ls and rs
    ls = maxPathSumUtil(root.left, res)
    rs = maxPathSumUtil(root.right, res)

    # If both left and right children exist
    if root.left is not None and root.right is not None:
        # update result if needed
        res[0] = max(res[0], ls + rs + root.data)

        # Return maximum possible value for root being
        # on one side
        return max(ls, rs) + root.data

    # If any of the two children is empty, return
    # root sum for root being on one side
    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data


# The main function which returns sum of the maximum
# sum path betwee ntwo leaves. THis function mainly
# uses maxPathSumUtil()


def maxPathSum(root):
    res = [INT_MIN]
    maxPathSumUtil(root, res)
    return res[0]


def insert(tree_root: Node, new):

    if tree_root is None:
        return Node(new)

    cur = tree_root
    while cur is not None:
        cur = cur.left


if __name__ == '__main__':


    """
    n = int(input())
    data = []
    root = Node(data[0])
    for new_value in data:
        root = insert(root, new_value)
    """

    root = Node(36)
    root.left = Node(21)
    root.right = Node(15)

    root.left.left = Node(10)
    root.left.right = Node(19)
    root.right.left = Node(30)
    root.right.right = Node(20)

    root.left.left.left = Node(14)
    root.left.left.right = Node(6)
    root.left.right.left = Node(11)
    root.left.right.right = Node(5)
    root.right.left.left = Node(9)
    root.right.left.right = Node(10)
    root.right.right.left = Node(2)
    root.right.right.right = Node(7)

    print(maxPathSum(root))
