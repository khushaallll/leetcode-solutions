"""
Template for solving a tree problem locally.
Copy this file for each new problem.
"""

from typing import Optional
from treeutils import TreeNode, build_tree, to_list, print_tree, find_node


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        
        if not root.left and not root.right:
            return root
        
        left_node = self.invertTree(root.left)
        right_node = self.invertTree(root.right)
        root.right = left_node
        root.left = right_node
        return root


if __name__ == "__main__":
    s = Solution()

    # (input list, expected answer)
    tests = [
        ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
        # ([], []),          # empty tree
        # ([2,1,3], [2,3,1])  # root with two children
    ]

    root = build_tree(tests[0])
    got = s.invertTree(root)

    # for values, expected in tests:
    #     root = build_tree(values)
    #     got = s.invertTree(root)
    #     got_tree = build_tree(got)
    #     status = "PASS" if got_tree == expected else "FAIL"
    #     print(f"{status}  input={values}  expected={expected}  got={got}")
    #     if status == "FAIL":
    #         print_tree(root)   # show the tree that failed
