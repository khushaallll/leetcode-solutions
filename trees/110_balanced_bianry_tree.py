"""
Template for solving a tree problem locally.
Copy this file for each new problem.
"""

from typing import Optional
from treeutils import TreeNode, build_tree, to_list, print_tree, find_node


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        
        def node_depth(node: TreeNode | None): 
            if not node: 
                return 0                        #base case - empty tree

            left = node_depth(node.left)        # if left tree - unbalanced
            if left == -1:
                return -1
            
            right = node_depth(node.right)      # if right tree - unbalanced
            if right == -1:
                return -1
            
            if abs(left - right) > 1:           # if current tree found unbalanced
                return -1
            
            return 1 + max(left, right)     # if not unbalanced, return height of current subtree

        return node_depth(root) != -1

if __name__ == "__main__":
    s = Solution()

    # (input list, expected answer)
    tests = [
        ([3,9,20,None,None,15,7],True), 
        ([1,2,2,3,3,None,None,4,4], False),
        ([], True) 
    ]


    for values, op in tests:
        print(values, op)
        root = build_tree(values)
        got = s.isBalanced(root)
        print("passed?: ",got)
