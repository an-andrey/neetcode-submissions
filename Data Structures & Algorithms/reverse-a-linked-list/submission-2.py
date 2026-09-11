# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_ptr = head
        if curr_ptr is None: 
            return head

        prev_ptr = None
        next_ptr = head.next
        while next_ptr != None:
            curr_ptr.next = prev_ptr

            #move everything by 1
            prev_ptr = curr_ptr
            curr_ptr = next_ptr
            next_ptr = curr_ptr.next

        curr_ptr.next = prev_ptr

        return curr_ptr
        
            

