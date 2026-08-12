# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec_bst(node, lwr, gt):
            if not node:
                return True
            if lwr!=None and node.val >= lwr:
                return False
            if gt!=None and node.val <= gt:
                return False
            # if node.left and node.left.val >= node.val:
            #     return False
            # if node.right and node.right.val <= node.val:
            #     return False
            return rec_bst(node.left,node.val,gt ) and rec_bst(node.right, lwr, node.val)

        return rec_bst(root,None, None )