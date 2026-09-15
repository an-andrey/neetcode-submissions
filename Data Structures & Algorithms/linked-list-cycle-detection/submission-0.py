# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycles = set()

        ptr = head

        while ptr is not None and ptr not in cycles:
            cycles.add(ptr)
            ptr = ptr.next
        
        if ptr is None: 
            return False

        else:
            return True