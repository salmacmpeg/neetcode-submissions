# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findmin(self,list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None or list2 == None:
            return None
        if list1.val < list2.val :
            return list1
        return list2
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head = None
        list3 = None
        while list1 and list2:
                temp_max = self.findmin(list1,list2)
                if head == None:
                    head = list3 = temp_max
                else:
                    list3.next = temp_max
                    list3 = list3.next
                if temp_max == list1:
                    list1 = list1.next
                else:
                    list2 = list2.next
     
        if list1 != None:
            list3.next = list1
        if list2 != None:
            list3.next = list2
        return head