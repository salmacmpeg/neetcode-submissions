"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def rec_dfs(node):
            if not node:
                return None

            if node in self.visited:
                return self.visited[node]

            Newnode = Node(node.val)
            self.visited[node] = Newnode
            for nei in node.neighbors:
                Newnode.neighbors.append( rec_dfs(nei))

            return Newnode
        
        return rec_dfs(node) if node else None





