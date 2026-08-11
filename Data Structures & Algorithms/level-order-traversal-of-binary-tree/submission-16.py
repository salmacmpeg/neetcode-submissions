# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        all_list = []
        if not root:
            return []
        queue = deque()
        queue.append(root)
        while queue:
            listy= []
            curr_level= len(queue)
            while curr_level> 0: 
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                listy.append(node.val)
                curr_level -=1
            all_list.append(listy)
        return all_list