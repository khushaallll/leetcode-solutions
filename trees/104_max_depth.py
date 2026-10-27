"""
Template for solving a tree problem locally.
Copy this file for each new problem.
"""

from typing import Optional
from treeutils import TreeNode, build_tree, to_list, print_tree, find_node


class Solution:
    
    # # Top Down Approach
    # def maxDepth(self, root: TreeNode | None) -> int:
    #     self.max_depth = 0
        
    #     def dfs(node, depth) -> int:
    #         if not node:
    #             return

    #         if not node.left and not node.right:
    #             self.max_depth = max(self.max_depth, depth)

    #         dfs(node.left, depth + 1)
    #         dfs(node.right, depth + 1)

    #     dfs(root, 1)
    #     return self.max_depth

    # Bottom up approach
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1

        return max(left_depth, right_depth)
        

            
            
             


if __name__ == "__main__":
    s = Solution()

    # (input list, expected answer)
    tests = [
        [], 
        [1], 
        [1, 2, 3], 
        [3, 9, 20, None, None, 15, 7], 
        [1, None, 2, None, 3]
    ]


    for values in tests:
        root = build_tree(values)
        got = s.maxDepth(root)
        print(got)
