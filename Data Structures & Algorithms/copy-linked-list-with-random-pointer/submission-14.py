"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        hashmap = {}
        ptr = head
        while ptr :
            newNode = Node(ptr.val, None, None)
            hashmap [ptr] = newNode
            ptr = ptr.next
        
        ptr = head
        curnode = None
        while ptr.next :
            nxtptr = ptr.next
            nxtnode = hashmap[nxtptr]
            curnode = hashmap[ptr]
            curnode.next = nxtnode
            if ptr.random:
                curnode.random = hashmap[ptr.random]
            else:
                curnode.random = None
            ptr = ptr.next
        
        curnode = hashmap[ptr]
        if ptr.random:
            curnode.random = hashmap[ptr.random]
        else:
            curnode.random = None
            
        return hashmap[head]