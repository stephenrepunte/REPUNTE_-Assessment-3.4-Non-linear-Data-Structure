"""
Non-Linear Data Structure (Assessment 3.3)
Asks for the last name, then runs the Binary Tree and the Graph.
Each structure lives in its own file: binary_tree.py and graph.py
"""
import binary_tree
import graph


def main():
    last_name = input("Enter your last name: ").strip().upper()
    print(f"\nLast name: {last_name}\n")

    binary_tree.run()
    print()
    graph.run()


if __name__ == "__main__":
    main()
