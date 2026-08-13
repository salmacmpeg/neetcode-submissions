# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_val = -2000
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def rec_helper(node):
            #decide whether to add my self or not ?
            if not node:
                return 0
            
            left_val = max(rec_helper(node.left),0)
            right_val = max(rec_helper(node.right),0)

            path1= left_val+node.val+right_val
            path2= left_val+node.val
            path3= node.val+right_val

            self.max_val = max(self.max_val, path1, path2, path3)

            return max(path2,path3)

        rec_helper(root)
        
        return  self.max_val