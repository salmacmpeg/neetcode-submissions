# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_identical(nroot, nsubRoot):
            if (not nroot and nsubRoot) or (nroot and not nsubRoot):
                return False
            if not nroot and not nsubRoot:
                return True
            if nroot.val == nsubRoot.val:
                return is_identical(nroot.left, nsubRoot.left) and is_identical(nroot.right, nsubRoot.right)
            else:
                return False
        found = False
        
        found = found or is_identical(root, subRoot)
        if root.left: found = found or self.isSubtree(root.left, subRoot)
        if root.right: found = found or self.isSubtree(root.right, subRoot)
        return found