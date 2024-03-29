# Python program to find maximumpath sum between two leaves
# of a binary tree
from binarytree import build

INT_MIN = -2**32

# A binary tree node


class Node:
	# Constructor to create a new node
	def __init__(self, val):
		self.val = val
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
		res[0] = max(res[0], ls + rs + root.val)

		# Return maximum possible value for root being
		# on one side
		return max(ls, rs) + root.val

	# If any of the two children is empty, return
	# root sum for root being on one side
	if root.left is None:
		return rs + root.val
	else:
		return ls + root.val

# The main function which returns sum of the maximum
# sum path betwee ntwo leaves. THis function mainly
# uses maxPathSumUtil()


def maxPathSum(root):
	res = [INT_MIN]
	maxPathSumUtil(root, res)
	return res[0]


# Driver program to test above function
root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)

root.right.right.right.right.left = Node(10)

print("Max pathSum of the given binary tree is " + str(maxPathSum(root)))

# my_tree = build([10, 15, 19, 21, 20, 30, 14, 36, 5, 11, 9, 6, 2, 10, 7])
my_tree = build([36, 21, 6, 15, 30, 11, 10, 10, 19, 20, 14, 5, 9, 2, 7])
print(my_tree)
print('max: ' + str(maxPathSum(my_tree)))
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
