# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        global_minimums = [(lists[i].val, i) for i in range(len(lists)) if lists[i] is not None] 
        out_root = None
        ptr = None

        heapq.heapify(global_minimums)

        while global_minimums: 
            val, i = heapq.heappop(global_minimums)
            root = lists[i]
            lists[i] = root.next
            
            if out_root is None: 
                out_root = root
                ptr = out_root
            else:
                ptr.next = root
                ptr = ptr.next

            if lists[i] is not None: 
                heapq.heappush(global_minimums, (lists[i].val, i))

        return out_root

        

        

                
            