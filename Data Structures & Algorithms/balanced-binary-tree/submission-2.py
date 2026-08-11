# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True

        def rec_hight(node):
            if not node:
                return 0
            
            left_h = rec_hight(node.left)
            right_h = rec_hight(node.right)

            if abs(left_h - right_h) > 1:
                self.bal = False

            return 1+max(left_h,right_h)

        rec_hight(root)
        return self.bal