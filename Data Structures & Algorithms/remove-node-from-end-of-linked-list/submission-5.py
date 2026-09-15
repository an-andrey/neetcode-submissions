# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_prev = head
        curr = head

        for i in range(n): 
            curr = curr.next

        if curr is None: 
            return head.next

        while curr.next != None:
            n_prev = n_prev.next
            curr = curr.next

        n_prev.next = n_prev.next.next

        return head

         