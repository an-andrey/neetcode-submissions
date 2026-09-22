# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # go to middle, reverse the list, merge
        
        def revLL(head): 
            prev = None
            curr = head

            while curr:
                curr.next, curr, prev = prev, curr.next, curr

            return prev

        hop, curr = head, head

        while hop and hop.next:
            hop = hop.next.next
            curr = curr.next
        
        head2 = curr.next
        curr.next = None
        head2 = revLL(head2)

        ptr = head 
        while head2: 
            next1 = ptr.next
            next2 = head2.next

            ptr.next = head2
            head2.next = next1

            ptr = next1
            head2 = next2

            


                
                