class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInOrder(root, lis):
    if root == None:
        return
    printInOrder(root.left, lis)
    lis.append(root.val)
    printInOrder(root.right, lis)


def printPreOrder(root, lis):
    if root == None:
        return
    lis.append(root.val)
    printPreOrder(root.left, lis)
    printPreOrder(root.right, lis)


def printPostOrder(root, lis):
    if root == None:
        return
    printPostOrder(root.left, lis)
    printPostOrder(root.right, lis)
    lis.append(root.val)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
lis = []
printPreOrder(tree, lis)
print(lis)
lis = []
printInOrder(tree, lis)
print(lis)
lis = []
printPostOrder(tree, lis)
print(lis)

#        1
#      2   3
#    4   5
