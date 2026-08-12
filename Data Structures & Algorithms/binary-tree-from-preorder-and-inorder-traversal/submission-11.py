# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    indx_glp = -1
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashy= {val:i for i,val in enumerate(inorder)}
        def rec_dfs(left, right):
            if left>right:
                return None
            self.indx_glp+=1
            elem = preorder[self.indx_glp]
            hashy_k = hashy[elem]
            node = TreeNode(elem, None, None)
            node.left = rec_dfs(left,hashy_k-1)
            node.right = rec_dfs(hashy_k+1, right)
            
            return node
        
        return rec_dfs(0, len(inorder)-1 )








