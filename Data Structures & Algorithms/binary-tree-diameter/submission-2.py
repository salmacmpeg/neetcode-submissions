# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs_tree(node):
            if not node:
                return 0
            left_depth = dfs_tree(node.left)
            right_depth = dfs_tree(node.right)
            self.res = max(self.res, (left_depth+right_depth) )
            return 1 + max(left_depth, right_depth)

        dfs_tree(root)
        return self.res