# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        hash_table ={}
        temp = head
        while temp.next:
            x = hash_table.get(temp.next, -1)
            if x != -1:
                return True
            hash_table[temp.next] = 1
            temp =temp.next
        return False

        