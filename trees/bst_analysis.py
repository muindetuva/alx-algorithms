#!/usr/bin/python3
"""Build and inspect BSTs created from three insertion orders."""

from dataclasses import dataclass


@dataclass
class Node:
    """Store one BST value and its child references."""

    value: int
    left: object = None
    right: object = None


class BinarySearchTree:
    """A basic unbalanced binary search tree for shape analysis."""

    def __init__(self):
        """Create an empty tree."""
        self.root = None

    def insert(self, value):
        """Insert one unique value using standard BST comparisons."""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                return

    def height(self):
        """Return height in node levels; an empty tree has height zero."""
        def node_height(node):
            if node is None:
                return 0
            return 1 + max(node_height(node.left), node_height(node.right))

        return node_height(self.root)

    def inorder(self):
        """Return all values using left-root-right traversal."""
        values = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            values.append(node.value)
            visit(node.right)

        visit(self.root)
        return values

    def search_comparisons(self, value):
        """Return comparisons made by a successful or failed BST search."""
        comparisons = 0
        current = self.root
        while current is not None:
            comparisons += 1
            if value == current.value:
                return comparisons
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return comparisons

    def worst_case_search_cost(self):
        """Return the largest successful-search comparison count."""
        if self.root is None:
            return 0
        return max(self.search_comparisons(value) for value in self.inorder())

    def print_sideways(self):
        """Print right children above parents and left children below."""
        def print_node(node, depth):
            if node is None:
                return
            print_node(node.right, depth + 1)
            print(f"{'    ' * depth}{node.value}")
            print_node(node.left, depth + 1)

        print_node(self.root, 0)


SEQUENCES = {
    "A — Balanced": [50, 25, 75, 10, 40, 60, 90],
    "B — Ascending": [10, 25, 40, 50, 60, 75, 90],
    "C — Mixed": [10, 90, 25, 75, 40, 60, 50],
}


def build_tree(sequence):
    """Build and return a BST from sequence order."""
    tree = BinarySearchTree()
    for value in sequence:
        tree.insert(value)
    return tree


def run_analysis():
    """Print shape, traversal, height, and cost for every sequence."""
    results = {}
    for name, sequence in SEQUENCES.items():
        tree = build_tree(sequence)
        height = tree.height()
        cost = tree.worst_case_search_cost()
        traversal = tree.inorder()
        results[name] = {
            "height": height,
            "worst_case_search": cost,
            "inorder": traversal,
        }
        print(name)
        tree.print_sideways()
        print(f"In-order: {traversal}")
        print(f"Height (node levels): {height}")
        print(f"Worst-case successful search comparisons: {cost}\n")
    return results


if __name__ == "__main__":
    run_analysis()
