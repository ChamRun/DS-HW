import binarytree


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_path(tree, cur_sum):
    if tree is None:
        return 0, None

    cur_sum += tree.val

    # print('f: ' + str(tree.val))
    left_f, l_path_leaf = max_path(tree.left, cur_sum)
    right_f, r_path_leaf = max_path(tree.right, cur_sum)

    max_kid = max(right_f, left_f)

    if r_path_leaf is None:
        path_leaf = tree.val
    elif max_kid == right_f:
        path_leaf = r_path_leaf
    else:
        path_leaf = l_path_leaf

    max_sum = tree.val + max_kid

    return max_sum, path_leaf


def pre_past_to_tree(preorder, postorder, left, h):
    global index

    if len(preorder) < index or h < left:
        return None

    tree = Node(preorder[index])
    index += 1

    if left == h or len(preorder) <= index:
        return tree

    for j in range(left, h + 1):
        if preorder[index] == postorder[j]:
            if j <= h:
                tree.left = pre_past_to_tree(preorder, postorder, left, j)
                tree.right = pre_past_to_tree(preorder, postorder, j + 1, h - 1)

            break

    return tree


def clear_path(root, target_leaf):
    if root is None:
        return False

    if (root.val == target_leaf or
            clear_path(root.left, target_leaf) or
            clear_path(root.right, target_leaf)):
        root.val = 0
        return True

    return False


index = 0


def main():
    n = int(input())

    for i in range(n):
        global index
        index = 0

        data0 = input()
        data1 = input()

        data0 = data0.replace(',', '')
        data1 = data1.replace(',', '')

        pre_order = [int(x) for x in data0.split()[1:]]
        # print(pre_numbers)
        past_order = [int(x) for x in data1.split()[1:]]
        # print(past_numbers)

        # print(data0.split()[0])
        if data0.split()[0] == 'post:':
            past_order, pre_order = pre_order, past_order

        my_tree = pre_past_to_tree(pre_order, past_order, 0, len(pre_order))

        # print(pre_order)
        # print(past_order)
        # print(my_tree)
        # f(my_tree, maximum)

        max_sum1, path_leaf = max_path(my_tree, 0)
        # print('path_leaf: ')
        # print(path_leaf)
        clear_path(my_tree, path_leaf)
        # print(my_tree)
        max_sum2, path_leaf = max_path(my_tree, 0)

        # print(str(i) + 'th ans: ' + str(max(pre_maximum, past_maximum)))
        print(str(max_sum1 + max_sum2))
        # print('\n')


if __name__ == '__main__':
    main()
