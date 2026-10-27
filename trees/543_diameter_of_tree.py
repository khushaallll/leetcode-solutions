"""
Template for solving a tree problem locally.
Copy this file for each new problem.
"""

from typing import Optional
from treeutils import TreeNode, build_tree, to_list, print_tree, find_node


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def diameter(node: TreeNode):
            if not node:
                return 0

            left = diameter(node.left)
            right = diameter(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1+ max(left, right)

        diameter(root)
        return self.diameter

        

if __name__ == "__main__":
    s = Solution()

    # (input list, expected answer)
    tests = [
        ([1,2,3,4,5],3), 
        ([1,2], 1), 
    ]


    for values, op in tests:
        root = build_tree(values)
        got = s.diameterOfBinaryTree(root)
        print("Answer: ",got)
