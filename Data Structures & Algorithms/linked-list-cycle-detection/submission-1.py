# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycles = set()

        while True:
            if head is None: 
                return False
            elif head in cycles:
                return True

            cycles.add(head)
            head = head.next
        
        