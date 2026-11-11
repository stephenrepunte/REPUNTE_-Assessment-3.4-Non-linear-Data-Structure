r"""
Binary Tree structure (Assessment 3.3)

           R
         /   \
        E     P
       / \   / \
      U   N T   E
"""
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def build(self):
        """Algorithm 1A: build the tree from the diagram."""
        self.root = Node("R")
        self.root.left = Node("E")
        self.root.right = Node("P")
        self.root.left.left = Node("U")
        self.root.left.right = Node("N")
        self.root.right.left = Node("T")
        self.root.right.right = Node("E")

    def bfs(self):
        """Algorithm 1B: level-order traversal using a queue."""
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs(self):
        """Algorithm 1C: preorder traversal (Root -> Left -> Right)."""
        result = []
        self._dfs_visit(self.root, result)
        return result

    def _dfs_visit(self, node, result):
        if node is None:
            return
        result.append(node.data)
        self._dfs_visit(node.left, result)
        self._dfs_visit(node.right, result)


def run():
    """Build the tree and print its traversals."""
    tree = BinaryTree()
    tree.build()
    print("=== BINARY TREE ===")
    print("BFS:", " -> ".join(tree.bfs()))
    print("DFS:", " -> ".join(tree.dfs()))


if __name__ == "__main__":
    run()
