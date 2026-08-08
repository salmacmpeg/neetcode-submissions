# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        iter_ptr = head
        temp_ptr = iter_ptr.next
        iter_ptr.next = None
        while temp_ptr :
            temp_next = temp_ptr.next
            temp_ptr.next = iter_ptr
            iter_ptr = temp_ptr
            temp_ptr= temp_next
 
        return iter_ptr
