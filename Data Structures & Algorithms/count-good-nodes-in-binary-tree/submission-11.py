# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_val= -200
    num = 0
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        if root.val >= self.max_val:
            #iam a good node
            self.num += 1
            self.max_val = root.val
            num1 = self.goodNodes(root.left)
            self.max_val = root.val
            return 1 + num1 +self.goodNodes(root.right)
        else:
            temp = self.max_val
            num1= self.goodNodes(root.left)
            self.max_val = temp
            return  num1+self.goodNodes(root.right)
        return self.num