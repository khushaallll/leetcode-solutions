"""
treeutils.py - helpers for solving LeetCode tree problems locally.

Usage:
    from treeutils import TreeNode, build_tree, to_list, print_tree, find_node

    root = build_tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
    print_tree(root)
    print(to_list(root))     # [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    """Same class LeetCode gives you."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Makes print(node) show "TreeNode(8)" instead of a memory address.
        return f"TreeNode({self.val})"


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a tree from a LeetCode-style list (level order, None = no child).

    How it works:
      - The first value is the root.
      - A queue holds nodes that are still waiting for their children.
      - For each waiting node, the next two values in the list are its
        left child and right child. None means "no child here".
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Turn a tree back into a LeetCode-style list.
    Useful for checking answers of problems that return a tree
    (for example: Invert Binary Tree, BST insert/remove).
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # LeetCode drops the None values at the end.
    while result and result[-1] is None:
        result.pop()

    return result


def print_tree(root: Optional[TreeNode]) -> None:
    """
    Print the tree so you can see its shape. L = left child, R = right child.

        8
        ├── L: 3
        │   ├── L: 1
        │   └── R: 6
        └── R: 10
            └── R: 14
    """
    if not root:
        print("(empty tree)")
        return

    print(root.val)

    def walk(node, prefix):
        children = [(side, child)
                    for side, child in (("L", node.left), ("R", node.right))
                    if child]
        for index, (side, child) in enumerate(children):
            is_last = index == len(children) - 1
            branch = "└── " if is_last else "├── "
            print(f"{prefix}{branch}{side}: {child.val}")
            walk(child, prefix + ("    " if is_last else "│   "))

    walk(root, "")


def find_node(root: Optional[TreeNode], val) -> Optional[TreeNode]:
    """
    Return the first node with this value (searches the whole tree).
    Some problems take nodes as input, not values
    (for example: Lowest Common Ancestor). Use this to get them.
    """
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


if __name__ == "__main__":
    # Quick self-check: run `python treeutils.py`
    sample = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
    root = build_tree(sample)

    print_tree(root)
    print()
    print("to_list:", to_list(root))
    assert to_list(root) == sample, "round trip failed"

    assert build_tree([]) is None
    assert to_list(build_tree([1, None, 2])) == [1, None, 2]
    assert find_node(root, 6).val == 6
    assert find_node(root, 99) is None

    print("All checks passed.")
