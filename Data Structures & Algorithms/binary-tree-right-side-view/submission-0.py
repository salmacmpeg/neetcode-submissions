# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        all_list =[]
        queue = deque()
        queue.append(root)
        while queue:
            curr = len(queue)
            res =0
            while curr >0 :
                node = queue.popleft()
                res = node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                curr -= 1
            all_list.append(res)
        return all_list