"""
Template for solving a tree problem locally.
Copy this file for each new problem.
"""

from typing import Optional
from treeutils import TreeNode, build_tree, to_list, print_tree, find_node


class Solution:
    # Example problem: count the nodes in a tree.
    # Replace this method with the one from the LeetCode problem.
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == "__main__":
    s = Solution()

    # (input list, expected answer)
    tests = [
        ([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13], 9),
        ([], 0),          # empty tree
        ([1], 1),         # one node
        ([1, 2, 3], 3),   # root with two children
    ]

    for values, expected in tests:
        root = build_tree(values)
        got = s.countNodes(root)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}  input={values}  expected={expected}  got={got}")
        if status == "FAIL":
            print_tree(root)   # show the tree that failed
