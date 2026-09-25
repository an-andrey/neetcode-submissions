# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()

        if root: 
            queue.append(root)
        else: 
            return []
            
        output = []
        
        while len(queue): 
            level = []

            for _ in range(len(queue)):
                ptr = queue.popleft()
                level.append(ptr.val)

                if ptr.left: 
                    queue.append(ptr.left)
                if ptr.right: 
                    queue.append(ptr.right)

            output.append(level)

        return output



            
