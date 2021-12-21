from binarytree import Node

# Python3 program for construction of
# full binary tree

# A binary tree node has data, pointer
# to left child and a pointer to right child


# A recursive function to construct
# Full from pre[] and post[].
# preIndex is used to keep track
# of index in pre[]. l is low index
# and h is high index for the
# current subarray in post[]
def constructTreeUtil(pre: list, post: list,
                      l: int, h: int,
                      size: int) -> Node:
    global preIndex

    # Base case
    if (preIndex >= size or l > h):
        return None

    # The first node in preorder traversal
    # is root. So take the node at preIndex
    # from preorder and make it root, and
    # increment preIndex
    root = Node(pre[preIndex])
    preIndex += 1

    # If the current subarray has only
    # one element, no need to recur
    if (l == h or preIndex >= size):
        return root

    # Search the next element
    # of pre[] in post[]
    i = l
    while i <= h:
        if (pre[preIndex] == post[i]):
            break

        i += 1

    # Use the index of element
    # found in postorder to divide
    # postorder array in two parts.
    # Left subtree and right subtree
    if (i <= h):
        root.left = constructTreeUtil(pre, post,
                                      l, i, size)
        root.right = constructTreeUtil(pre, post,
                                       i + 1, h - 1,
                                       size)

    return root


# The main function to construct
# Full Binary Tree from given
# preorder and postorder traversals.
# This function mainly uses constructTreeUtil()
def constructTree(pre: list,
                  post: list,
                  size: int) -> Node:
    global preIndex

    return constructTreeUtil(pre, post, 0,
                             size - 1, size)


# A utility function to print
# inorder traversal of a Binary Tree
def printInorder(node: Node) -> None:
    if (node is None):
        return

    printInorder(node.left)
    print(node.val, end=" ")

    printInorder(node.right)


# Driver code
if __name__ == "__main__":
    pre = [36, 21, 15, 10, 19, 30, 20, 14, 6, 11, 5, 9, 10, 2, 7]
    post = [10, 19, 15, 20, 14, 30, 21, 5, 9, 11, 2, 7, 10, 6, 36]

    size = len(pre)

    preIndex = 0

    root = constructTree(pre, post, size)

    print(root)

    print("Inorder traversal of "
          "the constructed tree: ")



    printInorder(root)

# This code is contributed by sanjeev2552
