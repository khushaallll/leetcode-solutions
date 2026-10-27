"""
Template for solving a tree problem locally.
Copy this file for each new problem.
"""

from typing import Optional
from treeutils import TreeNode, build_tree, to_list, print_tree, find_node


class Solution:
    # # bottom up
    # def sum_of_all(self, root: TreeNode | None) -> int:
    #     if not root:
    #         return 0
    #     left_node = self.sum_of_all(root.left) 
    #     right_node = self.sum_of_all(root.right)
    #     return root.val + left_node + right_node

    # top down
    def sum_of_all(self, root: TreeNode | None) -> int:
        self.total = 0

        def sum_node(node: TreeNode | None) -> int:
            if not node:
                self.total = self.total + 0
            else: 
                self.total = self.total + node.val
                sum_node(node.left)
                sum_node(node.right)

            return
        
        sum_node(root)
        return self.total

        

if __name__ == "__main__":
    s = Solution()

    # (input list, expected answer)
    tests = [
        ([],0), 
        ([1],1), 
        ([1, 2, 3],6), 
        ([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13], 73), 
    ]


    for values, op in tests:
        root = build_tree(values)
        got = s.sum_of_all(root)
        print("Answer: ",got)
