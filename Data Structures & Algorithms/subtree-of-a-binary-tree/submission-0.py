# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def bfs_check(root1, root2):
            queue1 = deque([root1])
            queue2 = deque([root2])

            while len(queue1) and len(queue2): 
                node1 = queue1.popleft()
                node2 = queue2.popleft()

                if node1.val != node2.val: 
                    return False
                
                if node1.left and node2.left: 
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                else: 
                    if (node1.left and not node2.left) or (not node1.left and node2.left):
                        return False
                        
                if node1.right and node2.right: 
                    queue1.append(node1.right)
                    queue2.append(node2.right)
                else: 
                    if (node1.right and not node2.right) or (not node1.right and node2.right):
                        return False
            return True

        if not root: 
            if subRoot: 
                return False
            else: 
                return True
        else: 
            if not subRoot: 
                return False

        queue = deque([root])
        while len(queue): 
            root = queue.popleft()

            if root.val == subRoot.val: 
                if bfs_check(root, subRoot): 
                    return True
            
            if root.left: 
                queue.append(root.left)
            if root.right: 
                queue.append(root.right)

        return False
        

            

                