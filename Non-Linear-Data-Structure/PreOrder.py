
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class PreOrderTree:
    def __init__(self):
        self.root = None

    def insert(self, letter):
        new_node = Node(letter)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            queue.append(current.right)

    # PreOrder: Root, Left, Right
    def preorder(self, node):
        if node is None:
            return

        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def display_tree(self, node, space=0):
        if node is None:
            return

        self.display_tree(node.right, space + 5)
        print(" " * space + node.data)
        self.display_tree(node.left, space + 5)


tree = PreOrderTree()

name = "STEPHENREPUNTE"

for letter in name:
    tree.insert(letter)

print("===== PREORDER TREE =====")
tree.display_tree(tree.root)

print("\nPreOrder Traversal:")
tree.preorder(tree.root)
print()
