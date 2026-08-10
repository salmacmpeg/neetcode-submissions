# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 1 
        last = head
        while(last.next):
            last = last.next
            sz += 1
        rmv_indx = sz -n
        if rmv_indx == 0:
            temp =head
            head = temp.next
            del temp
            return head
        i=0
        ptr = head
        while (i < (rmv_indx-1)):
            ptr =ptr.next
            i+=1
        node_rm = ptr.next
        if node_rm: 
            ptr.next = node_rm.next
            del node_rm
        return head