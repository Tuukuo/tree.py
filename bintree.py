class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)
    print(node.data, end=", ")

root = Node('10')
node1 = Node('30')
node2 = Node('25')
node3 = Node('40')
node4 = Node('8')
node5 = Node('15')
node6 = Node('12')
node7 = Node('18')

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5
node2.right = node6

node6.left = node7

print("preorderTraversal:")
preOrderTraversal(root)
    