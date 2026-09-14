# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        ptr = None

        if list1 is None: 
            return list2

        if list2 is None: 
            return list1

        else: 
            if list1.val < list2.val: 
                new_list = ListNode(val=list1.val)
                list1 = list1.next
            else: 
                new_list = ListNode(val=list2.val)
                list2 = list2.next
            
            ptr = new_list

        while list1 is not None or list2 is not None: 
            if list1 is None: 
                ptr.next = list2
                return new_list

            elif list2 is None:
                ptr.next = list1
                return new_list

            elif list1.val < list2.val: 
                ptr.next = ListNode(val=list1.val)
                ptr = ptr.next
                list1 = list1.next

            else: #list1.val >= list2.val 
                ptr.next = ListNode(val=list2.val)
                ptr = ptr.next
                list2 = list2.next
        
        return new_list

    