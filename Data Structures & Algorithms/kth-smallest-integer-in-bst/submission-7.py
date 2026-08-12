# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        node = root
        def rec_dfs(node):
            if not node:
                return
            rec_dfs(node.left)
            queue.append(node)
            rec_dfs(node.right)
        rec_dfs(root)
        i =0
        while i<k:
            node = queue.popleft()
            i += 1
        return node.val