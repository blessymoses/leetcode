"""
Tree implementation
"""


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


#      4
#     / \
#    5   6
#   /\   /\
#  7  N N  N
# / \
# N N

root = Node(4)
root.left = Node(5)
root.right = Node(6)

root.left.left = Node(7)

"""
In-order traversal

Left Root Right
Root is in between left and right
"""
inorder_result = []


def inorder(node):
    if node:
        inorder(node.left)
        inorder_result.append(node.value)
        inorder(node.right)


inorder(root)
print(
    *inorder_result,
    sep="  ",
)  # 7  5  4  6
"""
Pre-order traversal

Root Left Right
Root is followed by left and right
"""
preorder_result = []


def preorder(node):
    if node:
        preorder_result.append(node.value)
        preorder(node.left)
        preorder(node.right)


preorder(root)
print(
    *preorder_result,
    sep="  ",
)  # 4  5  7  6
"""
Post-order traversal

Left Right Root
Root is visited after left and right
"""
postorder_result = []


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        postorder_result.append(node.value)


postorder(root)
print(
    *postorder_result,
    sep="  ",
)  # 7  5  6  4
