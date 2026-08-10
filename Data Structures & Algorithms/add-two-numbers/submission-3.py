# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        charset1= ''
        charset2= ''
        ptr1 = l1
        ptr2 = l2
        while ptr1 or ptr2:
            if ptr1:
                charset1 += str(ptr1.val)
                ptr1 = ptr1.next
            if ptr2:
                charset2 +=str(ptr2.val)
                ptr2 = ptr2.next
        rev1 = charset1[::-1]
        rev2 = charset2[::-1]

        res = int(rev1) + int(rev2)

        res_str = str(res)
        res_rvrs = res_str[::-1]
        head = None
        for char in res_rvrs:
            newNode = ListNode(int(char), None)
            if not head:
                head= newNode
            else:
                prev.next = newNode
            prev = newNode

        return head
