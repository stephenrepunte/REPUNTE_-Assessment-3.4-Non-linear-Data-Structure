
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class InOrderTree:
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

    # InOrder: Left, Root, Right
    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

    def display_tree(self, node, space=0):
        if node is None:
            return

        self.display_tree(node.right, space + 5)
        print(" " * space + node.data)
        self.display_tree(node.left, space + 5)


tree = InOrderTree()

name = "STEPHENREPUNTE"

for letter in name:
    tree.insert(letter)

print("===== INORDER TREE =====")
tree.display_tree(tree.root)

print("\nInOrder Traversal:")
tree.inorder(tree.root)
print()
