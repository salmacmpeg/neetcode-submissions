# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mystack = []
        tempf = head
        n =0
        while tempf:
            mystack.append(tempf)
            tempf = tempf.next
            n+=1
        tempf = head
        length = n//2
        if n <=1:
            return 
        back = None
        for i in range(length):
            front = tempf
            back = mystack.pop()
            tempf = tempf.next
            front.next = back
            back.next = tempf
        if n%2==0:
            back.next =None
        else:
            back = back.next
            back.next = None






